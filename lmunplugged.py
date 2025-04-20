from svg import SVG, Polygon, Rect, Circle, ViewBoxSpec
from random import random, shuffle
from numpy import linspace
from  matplotlib._color_data import XKCD_COLORS
from random import choice

def resolve_color(color):
    if color[0] == '#':
        return color
    else:
        return XKCD_COLORS['xkcd:'+color]

bin_fill_color = "#eeeeee"
bin_edge_color = "#595959"
class Coordinate:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __add__(self,change):
        if isinstance(change,tuple):
            # add to the location if a list of numbers
            return Coordinate(self.x + change[0],self.y + change[1])
        elif isinstance(change,Coordinate):
            return Coordinate(self.x + change.x,self.y + change.y)
        else:
            return NotImplemented
        
    def get_xy(self):
        return self.x,self.y
    
    def is_far(self,compare,dist):
        # TODO use proper distance
        if isinstance(compare,tuple):
            dx = abs(self.x-compare[0])
            dy = abs(self.y - compare[1])
            # print(dx,dy)
            return (dx > dist) and (dy > dist)
        elif isinstance(compare,Coordinate):
            dx = abs(self.x-compare.x)
            dy = abs(self.y - compare.y)
            # print(dx,dy)
            return (dx > dist)and (dy > dist)
        else:
            return NotImplemented
    
    def __str__(self):
        return f"({self.x},{self.y})"


class ImgObj:

    def set_location(self,new_location):
        self.location = new_location
    
    def render_obj(self):

        min_width, min_height = self.get_min_dims()
        
        return SVG(
            viewBox=ViewBoxSpec(0, 0, min_width+Bin.pad, min_height+Bin.pad),
            elements=self.get_elements(),)
    
    def render(self):
        return self.render_obj().as_str()
    


class Table(ImgObj):
    def __init__(self, bin_list,bin_spacing=5,bin_tops=0):
        '''
        '''
        self.bins ={cur_bin.name:cur_bin for cur_bin in bin_list} 
        # move bins so that they do not overlap
        num_bins = len(bin_list)
        bin_locations = [Coordinate(x*(Bin.bin_w_top+bin_spacing),bin_tops) for x in range(num_bins)]
        for cur_bin, cur_loc in zip(bin_list,bin_locations):
            cur_bin.set_location(cur_loc)

    def get_elements(self):
        return  [ei for it in self.bins.values() for ei in it.get_elements()]
    
    def get_min_dims(self):
        item_far_pts = PointList([it.get_min_dims() for it in self.bins.values()])
        return item_far_pts.get_min_dims()
    
    def sample_bin(self,name):
        return self.bins[name].sample()
    
    

class Bin(ImgObj):
    bin_w_top = 140
    bin_bottom_offset = round(.25*bin_w_top)
    bin_h = 140
    sticky_width = 30
    sticky_height = 20
    sticky_offset = 10
    pad = 5
    def __init__(self,color,left_x=0,top_y=0,contents=None):
        # Define dimensions and central positions for bin components
        self.color = resolve_color(color)
        self.name = color
        self.location = Coordinate(left_x,top_y)
        self.base_points = PointList([(0,0), (Bin.bin_bottom_offset, Bin.bin_h), 
                                 (Bin.bin_w_top-Bin.bin_bottom_offset, Bin.bin_h), (Bin.bin_w_top, 0)]) 
        

        self.contents = []
        self.compute_coodinates()
        if contents:
            # place balls relatively
            for ball in contents:
                ball.set_location(self.coordinates[len(self.contents)])
                self.contents.append(ball)
                # self.add_ball(ball)
        
        
        
    def get_elements(self):
        bin_points = self.base_points + self.location 
        # Define the main bin polygon and top rectangle part
        bin_polygon = Polygon(points=bin_points.points, 
                    fill=bin_fill_color,
                    stroke=bin_edge_color,
                    stroke_width=1)
        
        sticky_loc = self.location + (Bin.sticky_offset,0)
        sticky = Rect(x=sticky_loc.x,y=sticky_loc.y, 
                      width=Bin.sticky_width, height=Bin.sticky_height,
                      fill=self.color, stroke="transparent")
        
        # move balls relatively and get their elements
        contents = [item.get_elements(self.location) for item in self.contents]
        
        return [bin_polygon,sticky] +contents
    
    def get_min_dims(self):
        bin_points = self.base_points + self.location 
        return bin_points.get_min_dims()
    
    def sample(self):
        return choice(self.contents).name
        

    def add_ball(self,ball):
        
        ball.set_location(self.coordinates[len(self.contents)])
        self.contents.append(ball)

    
    def compute_coodinates(self):
        width_diff = 2*Bin.bin_bottom_offset
        center_min_width = Bin.bin_w_top -width_diff - 2*Bin.pad -2*Ball.radius
        usable_min_width = Bin.bin_w_top -2*Bin.bin_bottom_offset - 2*Bin.pad
        left_at_height = lambda y: y*Bin.bin_bottom_offset + Ball.radius + Bin.pad
        usable_width_at_height = lambda y: (1-y)*width_diff + usable_min_width
        center_width_at_height = lambda y: (1-y)*width_diff + center_min_width
        usable_height = Bin.bin_h-(Bin.pad+Bin.sticky_height)
        center_usable_height = usable_height-2*Ball.radius
        max_vert_balls = usable_height//(2*(Ball.radius+Ball.pad))
        # bias to bottom
        balls_at_height = lambda y: int(usable_width_at_height(y)//(2*(Ball.radius+Ball.pad)))

        coords = [[Coordinate(left_at_height(rel_y)+x,rel_y*center_usable_height+Bin.pad+Bin.sticky_height)
                                for x in linspace(0,center_width_at_height(rel_y),num=balls_at_height(rel_y))]
                                            for rel_y in linspace(1,0,max_vert_balls) ]
        [shuffle(row) for row in coords]
        # TODO:  should be jittered too
        self.coordinates = [c for row in coords for c in row]
        
        
    @staticmethod
    def ball_loc_candidate(prev_placed):

        width_diff = 2*Bin.bin_bottom_offset
        min_width = Bin.bin_w_top -2*Bin.bin_bottom_offset - 2*Bin.pad -Ball.radius
        left_at_height = lambda y: y*Bin.bin_bottom_offset + Ball.radius + Bin.pad
        width_at_height = lambda y: (1-y)*width_diff + min_width
        usable_height = Bin.bin_h-(2*Ball.radius+Bin.pad+Bin.sticky_height)
        # random location within the height
        rel_y = random()
        candidate_y = rel_y*usable_height +Bin.pad + Ball.radius+Bin.sticky_height

        # random location within the width at that height 
        rel_x = random()
        candidate_x = rel_x*width_at_height(candidate_y) + left_at_height(candidate_y)
        return Coordinate(round(candidate_x),round(candidate_y))
    
    @staticmethod
    def get_ball_loc_ordered(self,prev_placed):
        width_diff = 2*Bin.bin_bottom_offset
        center_min_width = Bin.bin_w_top -2*Bin.bin_bottom_offset - 2*Bin.pad -Ball.radius
        usable_min_width = Bin.bin_w_top -2*Bin.bin_bottom_offset - 2*Bin.pad
        left_at_height = lambda y: y*Bin.bin_bottom_offset + Ball.radius + Bin.pad
        width_at_height = lambda y: (1-y)*width_diff + usable_min_width
        usable_height = Bin.bin_h-(Bin.pad+Bin.sticky_height)
        center_usable_height = usable_height-2*Ball.radius
        max_vert_balls = usable_height//(2*(Ball.radius+Ball.pad))
        # bias to bottom
        balls_at_height = lambda y: width_at_height(y)//(2*(Ball.radius+Ball.pad))
        # prev_bias = (1-prev_placed/)
    
class Doc(ImgObj):
    sticky_width = 100
    sticky_height = 60
    def __init__(self, word_list,word_spacing=10,word_tops=0):
        '''
        '''
        self.words = word_list 
        # move stickies so that they do not overlap
        self.num_words = len(word_list)
        self.word_spacing = word_spacing
        word_locations = [Coordinate(x*(Doc.sticky_width+word_spacing),word_tops) for x in range(self.num_words)]
        
        for cur_word, cur_loc in zip(word_list,word_locations):
            cur_word.set_location(cur_loc)

    def get_elements(self):
        return  [ei for it in self.words for ei in it.get_elements()]
    
    def get_min_dims(self):
        width = self.num_words*(Doc.sticky_width+self.word_spacing)
        height = Doc.sticky_height+2*self.word_spacing
        return width,height
    
    def add_word(self,color):
        last_word = self.words[-1]
        new_word = Sticky(color)
        new_word.set_location(last_word.location + Coordinate(Doc.sticky_width+self.word_spacing,0))
        self.words.append(new_word)
        self.num_words += 1
    

class Sticky(ImgObj):
    def __init__(self,color,left_x=0,top_y=0):
        # Define dimensions and central positions for bin components
        self.color = resolve_color(color)
        self.name = color
        self.location = Coordinate(left_x,top_y)
        
        

    
    def get_elements(self):
               
        x,y = self.location.get_xy() 
        sticky = Rect(x=x,y=y,
                      width=Doc.sticky_width, height=Doc.sticky_height,
                      fill=self.color, stroke="transparent")
        
        return [sticky] 

class Ball(ImgObj):
    radius = 10
    pad = 2
    def __init__(self,color,cx=radius,cy=radius):
        '''
        '''
        self.location = Coordinate(cx,cy)
        self.color = resolve_color(color)
        self.name = color
        
    
    def adjust(self,rel_location):
        self.location()
         
    
    def get_min_dims(self):
        far_loc = self.location + Coordinate(Ball.radius,Ball.radius)
        return far_loc.get_xy()
    
    def get_elements(self,adjust=Coordinate(0,0)):
        x,y = self.location.get_xy()
        dx,dy = adjust.get_xy()
        ball = Circle(
                cx=x+dx, cy=y+dy, r=Ball.radius,
                fill=self.color,
                stroke="transparent",
            )
        
        return [ball]
    
    def is_far(self,candidate):
        return self.location.is_far(candidate,self.radius+1)
    
    def __str__(self):
        return f"{self.color} at {self.location}"




        

class PointList:
    def __init__(self,point_list):
        self.points = point_list

    def __add__(self,to_add):
        '''
        '''
        if isinstance(to_add,tuple):
            # add to the location if a list of numbers
            dx = to_add[0]
            dy = to_add[1]
            new_points = [(xi+dx,yi+dy) for xi,yi in self.points]
            return PointList(new_points)
        elif isinstance(to_add,Coordinate):
            dx = to_add.x
            dy = to_add.y
            new_points = [(xi+dx,yi+dy) for xi,yi in self.points]
            return PointList(new_points)
        else:
            return NotImplemented
        
    def get_min_dims(self):
        w = max([xi for xi,_ in self.points])
        h = max([yi for _,yi in self.points])
        return w,h

import cadquery as cq
from keyhole_command_mount import generate_keyhole

base_overhang = 2

mounting_strip_width = 15.8
mounting_strip_height = 46.8

base_thickness = 3
base_width = mounting_strip_width + base_overhang * 2
base_height = mounting_strip_height + base_overhang * 2

large_diameter = 8.1
small_diameter = 4.2
depth = 5.25
length = 27
thickness = 2
separation = 29.2

tolerance = .25

obj = cq.Workplane().box(base_width, base_height, base_thickness)
obj = obj.box(separation + 2*large_diameter + base_overhang*2, length /2 + 10, base_thickness)
obj = obj.edges("|Z").fillet(4).faces(">Z").fillet(1).edges("<Z").chamfer(1)
obj = obj.union(generate_keyhole(large_diameter,small_diameter,depth,length/2,thickness).translate((-separation/2 - tolerance -large_diameter/2, 0, base_thickness/2)))
obj = obj.union(generate_keyhole(large_diameter,small_diameter,depth,length/2,thickness).translate((separation/2 + tolerance + large_diameter/2,0,base_thickness/2)))



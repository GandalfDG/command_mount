import cadquery as cq

base_overhang = 2

mounting_strip_width = 15.8
mounting_strip_height = 46.8

base_thickness = 3
base_width = mounting_strip_width + base_overhang * 2
base_height = mounting_strip_height + base_overhang * 2


keyhole_diameter_wide = 6.8
keyhole_diameter_narrow = 3.4
keyhole_full_depth = 3.8

bump_inset = 1.5
bump_radius = .5
keyhole_edge_depth = keyhole_full_depth - 1.6
tolerance = .25
keyhole_length = 15.9/2

mounting_base = (cq.Workplane("XY")
                 .box(mounting_strip_height,
                      mounting_strip_width,
                      base_thickness)
                 .edges("|Z").fillet(2).faces(">Z").fillet(.5))


def generate_keyhole(wide_diameter, narrow_diameter, slot_depth, slot_length, edge_thickness, fillet=.33, tolerance=.25):
    obj = cq.Workplane()

    slot_radius = narrow_diameter / 2 - tolerance
    keyhole_slot_depth = edge_thickness - tolerance

    # create the narrow keyhole slot
    obj = obj.slot2D(slot_length, narrow_diameter -
                     tolerance*2, 90).extrude(keyhole_slot_depth)

    # create the wide keyhole button
    obj = obj.faces(">Z").workplane().center(
         0, slot_length/2 - slot_radius,).tag("button_center")
    obj = obj.circle(wide_diameter/2 - tolerance).extrude(
        slot_depth - keyhole_slot_depth - tolerance)

    # fillet liberally
    obj = obj.faces("|Z and (not <Z)").fillet(fillet)

    return obj


# mounting_base = mounting_base.faces(">Z").workplane().union(generate_keyhole())
mounting_base = mounting_base.union(
    generate_keyhole(keyhole_diameter_wide, keyhole_diameter_narrow, keyhole_full_depth, keyhole_length, keyhole_edge_depth).translate(
        (mounting_strip_height/2 - 2*keyhole_diameter_wide, 0, base_thickness/2)))

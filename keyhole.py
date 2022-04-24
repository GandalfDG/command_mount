import cadquery as cq

def keyhole(self, wide_diameter, narrow_diameter, slot_depth, slot_length, edge_thickness, fillet=.33, tolerance=.25):

    def generate_keyhole():
        obj = self

        slot_radius = narrow_diameter / 2 - tolerance
        keyhole_slot_depth = edge_thickness - tolerance

        # create the narrow keyhole slot
        obj = obj.slot2D(slot_length, narrow_diameter -
                        tolerance*2, 0).extrude(keyhole_slot_depth)

        # create the wide keyhole button
        obj = obj.faces(">Z").workplane().center(
            slot_length/2 - slot_radius, 0).tag("button_center")
        obj = obj.circle(wide_diameter/2 - tolerance).extrude(
            slot_depth - keyhole_slot_depth - tolerance)

        # fillet liberally
        obj = obj.faces("|Z and (not <Z)").fillet(fillet)

        return obj

    return self.eachpoint(lambda loc: self.moveTo(loc).generate_keyhole(),True)
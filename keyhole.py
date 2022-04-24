import cadquery as cq

def keyhole(self, wide_diameter, narrow_diameter, slot_depth, edge_thickness, slot_length=None, fillet=0, tolerance=.25):

    slot_length = slot_length if slot_length else wide_diameter/2

    def generate_keyhole():
        obj = self.newObject()

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
        # obj = obj.faces("|Z and (not <Z)").fillet(fillet)

        # return obj.move(*loc.toTuple()[0])
        return obj.val()
    
    return self.eachpoint(lambda loc:generate_keyhole().moved(loc))

cq.Workplane.keyhole = keyhole
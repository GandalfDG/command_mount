import cadquery as cq


def keyhole(
        self, wide_diameter, narrow_diameter, slot_depth, edge_thickness,
        slot_length=None, fillet=.2, tolerance=.25):

    slot_length = slot_length if slot_length else wide_diameter/2

    def generate_keyhole():
        obj = cq.Workplane()

        slot_radius = narrow_diameter / 2 - tolerance
        keyhole_slot_depth = edge_thickness - tolerance

        # create the narrow keyhole slot
        obj = obj.slot2D(slot_length, narrow_diameter -
                         tolerance*2, 90).extrude(keyhole_slot_depth)

        # create the wide keyhole button
        obj = obj.faces(">Z").workplane().center(
            0, slot_length/2 - slot_radius).tag("button_center")
        obj = obj.circle(wide_diameter/2 - tolerance).extrude(
            slot_depth - keyhole_slot_depth - tolerance)

        # fillet liberally
        obj = obj.faces("|Z and (not <Z)").fillet(fillet)

        return obj.val()

    return self.eachpoint(
        lambda loc: generate_keyhole().moved(loc),
        combine=True)


cq.Workplane.keyhole = keyhole

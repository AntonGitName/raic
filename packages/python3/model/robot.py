class Robot:
    def __init__(self, json):
        self.id = json.get("id")
        self.player_id = json.get("player_id")
        self.is_teammate = json.get("is_teammate")
        self.x = json.get("x")
        self.y = json.get("y")
        self.z = json.get("z")
        self.velocity_x = json.get("velocity_x")
        self.velocity_y = json.get("velocity_y")
        self.velocity_z = json.get("velocity_z")
        self.radius = json.get("radius")
        self.nitro_amount = json.get("nitro_amount")
        self.touch = json.get("touch")
        self.touch_normal_x = json.get("touch_normal_x")
        self.touch_normal_y = json.get("touch_normal_y")
        self.touch_normal_z = json.get("touch_normal_z")

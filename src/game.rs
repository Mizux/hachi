pub struct Player {
    pub x: u16,
    pub y: u16,
}

pub struct GameState {
    pub player: Player,
    pub map_width: u16,
    pub map_height: u16,
}

impl GameState {
    pub fn new() -> Self {
        Self {
            player: Player { x: 5, y: 5 },
            map_width: 20,
            map_height: 10,
        }
    }

    pub fn move_player(&mut self, dx: i16, dy: i16) {
        let new_x = (self.player.x as i16 + dx).clamp(0, self.map_width as i16 - 1);
        let new_y = (self.player.y as i16 + dy).clamp(0, self.map_height as i16 - 1);
        self.player.x = new_x as u16;
        self.player.y = new_y as u16;
    }
}
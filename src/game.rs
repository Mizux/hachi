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
            map_width: 40,
            map_height: 20,
        }
    }

    pub fn move_player(&mut self, dx: i16, dy: i16) {
        let new_x = (self.player.x as i16 + dx).clamp(0, self.map_width as i16 - 1);
        let new_y = (self.player.y as i16 + dy).clamp(0, self.map_height as i16 - 1);
        self.player.x = new_x as u16;
        self.player.y = new_y as u16;
    }

    pub fn render_map(&self) -> String {
        let mut map_str = String::new();
        for y in 0..self.map_height {
            for x in 0..self.map_width {
                if x == self.player.x && y == self.player.y {
                    map_str.push_str("@ ");
                } else {
                    map_str.push_str(". ");
                }
            }
            if y < self.map_height - 1 {
                map_str.push('\n');
            }
        }
        map_str
    }
}
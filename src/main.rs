#[cfg(not(target_arch = "wasm32"))]
fn main() -> Result<(), Box<dyn std::error::Error>> {
    use crossterm::event::{self, Event, KeyCode};
    use ratatui::{backend::CrosstermBackend, widgets::Paragraph, Terminal};
    use hachi::game::GameState;

    crossterm::terminal::enable_raw_mode()?;
    let mut terminal = Terminal::new(CrosstermBackend::new(std::io::stdout()))?;
    let mut game = GameState::new();

    loop {
        terminal.draw(|f| {
            let info = format!("Player at ({}, {}) - Use WASD/Arrows to move, Q to quit", game.player.x, game.player.y);
            f.render_widget(Paragraph::new(info), f.area());
        })?;

        if let Event::Key(key) = event::read()? {
            match key.code {
                KeyCode::Char('w') | KeyCode::Up => game.move_player(0, -1),
                KeyCode::Char('s') | KeyCode::Down => game.move_player(0, 1),
                KeyCode::Char('a') | KeyCode::Left => game.move_player(-1, 0),
                KeyCode::Char('d') | KeyCode::Right => game.move_player(1, 0),
                KeyCode::Char('q') => break,
                _ => {}
            }
        }
    }

    crossterm::terminal::disable_raw_mode()?;
    Ok(())
}

#[cfg(target_arch = "wasm32")]
fn main() {}
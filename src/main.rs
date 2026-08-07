#[cfg(not(target_arch = "wasm32"))]
fn main() -> Result<(), Box<dyn std::error::Error>> {
    use crossterm::{
        event::{self, Event, KeyCode},
        execute,
        terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
    };
    use ratatui::{
        backend::CrosstermBackend,
        layout::{Constraint, Direction, Layout},
        widgets::{Block, Borders, Paragraph},
        Terminal,
    };
    use hachi::game::GameState;

    enable_raw_mode()?;
    let mut stdout = std::io::stdout();
    execute!(stdout, EnterAlternateScreen)?;
    let backend = CrosstermBackend::new(stdout);
    let mut terminal = Terminal::new(backend)?;
    let mut game = GameState::new();

    let res = (|| -> Result<(), Box<dyn std::error::Error>> {
        loop {
            terminal.draw(|f| {
                let main_chunks = Layout::default()
                    .direction(Direction::Horizontal)
                    .constraints([
                        Constraint::Length(game.map_width * 2 + 2), // Doubled width + borders
                        Constraint::Min(0),                         // Remaining right space
                    ])
                    .split(f.area());

                let map_chunks = Layout::default()
                    .direction(Direction::Vertical)
                    .constraints([
                        Constraint::Length(game.map_height + 2),
                        Constraint::Length(3), // Bottom HUD / status bar
                    ])
                    .split(main_chunks[0]);

                let map_widget = Paragraph::new(game.render_map())
                    .block(Block::default().borders(Borders::ALL).title("Hachi Map"));
                f.render_widget(map_widget, map_chunks[0]);

                let info = format!("Player at ({}, {}) - Use WASD/Arrows to move, Q to quit", game.player.x, game.player.y);
                let info_widget = Paragraph::new(info)
                    .block(Block::default().borders(Borders::ALL).title("Info"));
                f.render_widget(info_widget, map_chunks[1]);
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
        Ok(())
    })();

    disable_raw_mode()?;
    execute!(terminal.backend_mut(), LeaveAlternateScreen)?;
    terminal.show_cursor()?;
    res
}

#[cfg(target_arch = "wasm32")]
fn main() {}
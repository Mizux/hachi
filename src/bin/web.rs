#[cfg(target_arch = "wasm32")]
fn main() -> Result<(), Box<dyn std::error::Error>> {
    use std::{cell::RefCell, rc::Rc};
    use ratzilla::{
        event::KeyCode,
        ratatui::{
            layout::{Constraint, Direction, Layout},
            widgets::{Block, Borders, Paragraph},
            Terminal,
        },
        DomBackend, WebRenderer,
    };
    use hachi::game::GameState;

    let game = Rc::new(RefCell::new(GameState::new()));
    let backend = DomBackend::new()?;
    let mut terminal = Terminal::new(backend)?;

    terminal.on_key_event({
        let game = game.clone();
        move |key_event| {
            let mut g = game.borrow_mut();
            match key_event.code {
                KeyCode::Char('w') | KeyCode::Up => g.move_player(0, -1),
                KeyCode::Char('s') | KeyCode::Down => g.move_player(0, 1),
                KeyCode::Char('a') | KeyCode::Left => g.move_player(-1, 0),
                KeyCode::Char('d') | KeyCode::Right => g.move_player(1, 0),
                _ => {}
            }
        }
    })?;

    terminal.draw_web(move |f| {
        let g = game.borrow();
        let chunks = Layout::default()
            .direction(Direction::Vertical)
            .constraints([
                Constraint::Length(g.map_height + 2),
                Constraint::Length(3),
            ])
            .split(f.area());

        let map_widget = Paragraph::new(g.render_map())
            .block(Block::default().borders(Borders::ALL).title("Hachi Map"));
        f.render_widget(map_widget, chunks[0]);

        let info = format!("Player at ({}, {}) - Use WASD/Arrows to move", g.player.x, g.player.y);
        let info_widget = Paragraph::new(info)
            .block(Block::default().borders(Borders::ALL).title("Info"));
        f.render_widget(info_widget, chunks[1]);
    });

    Ok(())
}

#[cfg(not(target_arch = "wasm32"))]
fn main() {}
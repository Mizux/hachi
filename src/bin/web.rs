#[cfg(target_arch = "wasm32")]
fn main() -> Result<(), Box<dyn std::error::Error>> {
    use std::{cell::RefCell, rc::Rc};
    use ratzilla::{event::KeyCode, DomBackend, WebRenderer, ratatui::{widgets::Paragraph, Terminal}};
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
        let info = format!("Player at ({}, {})", g.player.x, g.player.y);
        f.render_widget(Paragraph::new(info), f.area());
    });

    Ok(())
}

#[cfg(not(target_arch = "wasm32"))]
fn main() {}
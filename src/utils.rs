use std::fs;
use std::path::PathBuf;
use serde::{Serialize, Deserialize};
use dirs; // needed for dirs::config_dir()
use std::io;

// Make Config public so it can be serialized/deserialized properly
#[derive(Serialize, Deserialize)]
pub struct Config {
    pub initial_usage: bool,
}

fn get_config_path() -> PathBuf {
    let mut path = dirs::config_dir().expect("Could not find config directory");
    path.push("shard-cli");
    fs::create_dir_all(&path).expect("Could not create config directory");
    path.push("config.json");
    path
}

fn load_config() -> Option<Config> {
    let config_path = get_config_path();
    if config_path.exists() {
        let data = fs::read_to_string(config_path).ok()?;
        serde_json::from_str(&data).ok()
    } else {
        None
    }
}

fn save_config(config: &Config) {
    let config_path = get_config_path();
    let data = serde_json::to_string_pretty(config).expect("Could not serialize config");
    fs::write(config_path, data).expect("Could not write config file");
}

pub fn initial_launch() {
    let mut config = load_config().unwrap_or(Config {
        initial_usage: true,
    });

    if !config.initial_usage {
        return; // they've seen the message before
    }

    println!("Hello, and welcome to Shard-CLI");
    println!("Would you like to take a quick tutorial? (y/n)");
    let mut input = String::new(); // create a mutable String to store input
        io::stdin()
            .read_line(&mut input)      // read input from stdin
            .expect("Failed to read line");
    
        let input = input.trim();       // remove newline and spaces
    
        if input.eq_ignore_ascii_case("y") {
            println!("Starting tutorial...");
        } else {
            println!("Skipping tutorial.");
        }

    // Mark as seen and save to config
    config.initial_usage = false;
    save_config(&config);
}

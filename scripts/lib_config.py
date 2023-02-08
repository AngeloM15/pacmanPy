"""Initial configuration of the session.

This script allows the user to configure the initial parameters
of the videogame.
"""

import os

import tomli

CONFIG_PATH = "/".join(os.path.abspath(__file__).split("/")[:-2]) + "/config"
ASSETS_PATH = "/".join(os.path.abspath(__file__).split("/")[:-2]) + "/assets"

CONF_FILE = {"config": "config.toml"}

CONF_FILE = {k: f"{CONFIG_PATH}/{v}" for k, v in CONF_FILE.items()}


class Config:
    """A class to load all the parameters for initial configuration."""

    screen_length: int
    screen_height: int

    black: list
    white: list
    blue: list
    red: list
    green: list

    stats: str
    characters: str

    lives: int

    def __init__(self):
        self.path = ASSETS_PATH
        self.config = self.load_config(CONF_FILE["config"])

        self.load_screen()
        self.load_color()
        self.load_sprites()
        self.load_stats()

    def load_config(self, f_name):
        """Load configuration from a specific TOML file.

        Parameters
        ----------
        f_name: str
            The name of the file to load.

        Returns
        -------
        config: dict
            A dictionary with configurations.
        """
        with open(f_name, mode="rb") as f_data:
            config = tomli.load(f_data)
        return config

    def load_screen(self):
        screen = self.config["screen"]

        self.screen_length = screen["length"]
        self.screen_height = screen["height"]

    def load_color(self):
        color = self.config["colors"]

        self.black = color["black"]
        self.white = color["white"]
        self.blue = color["blue"]
        self.red = color["red"]
        self.green = color["green"]

    def load_sprites(self):
        sprites = self.config["sprites"]

        self.group_1 = f'{ASSETS_PATH}/sprites/{sprites["group1"]}'
        self.group_2 = f'{ASSETS_PATH}/sprites/{sprites["group2"]}'

    def load_stats(self):
        character = self.config["character"]

        self.lives = character["lives"]

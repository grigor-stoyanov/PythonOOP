class Guild:
    players = []

    def __init__(self, name):
        self.name = name

    def assign_player(self, player):
        if not player.guild == self.name and player.guild == 'Unaffiliated':
            Guild.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif not player.guild == 'Unaffiliated':
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        for player in Guild.players:
            if player.name == player_name:
                Guild.players.remove(player)
                player.guild = 'Unaffiliated'
                return f"Player {player.name} has been removed from the guild."
        return f"Player {player.name} is not in the guild."

    def guild_info(self):
        return f'Guild: {self.name}\n' \
               f'{chr(10).join([player.player_info() for player in Guild.players])}'

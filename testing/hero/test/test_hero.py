import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero('abra', 12, 55.5, 66.6)
        self.enemy = Hero('cadabra', 12, 33.5, 43.6)

    def test_correct_init(self):
        self.assertEqual(self.hero.username, 'abra')
        self.assertEqual(self.hero.level, 12)
        self.assertEqual(self.hero.health, 55.5)
        self.assertEqual(self.hero.damage, 66.6)

    def test_battle_yourself_raises(self):
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.hero)
        self.assertEqual('You cannot fight yourself', str(e.exception))

    def test_battle_with_low_health_raises(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as e:
            self.hero.battle(self.enemy)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(e.exception))

    def test_battle_enemy_with_low_health_raises(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as e:
            self.hero.battle(self.enemy)
        self.assertEqual('You cannot fight cadabra. He needs to rest', str(e.exception))

    def test_battle_win(self):
        hero = Hero('abra', 1, 30, 40)
        enemy = Hero('cadabra', 1, 30, 20)
        self.assertEqual('You win', hero.battle(enemy))
        self.assertEqual(15, hero.health)
        self.assertEqual(2, hero.level)
        self.assertEqual(45, hero.damage)
        self.assertEqual(-10, enemy.health)

    def test_battle_lose(self):
        enemy = Hero('abra', 1, 30, 40)
        hero = Hero('cadabra', 1, 30, 20)
        self.assertEqual('You lose', hero.battle(enemy))
        self.assertEqual(15, enemy.health)
        self.assertEqual(2, enemy.level)
        self.assertEqual(45, enemy.damage)
        self.assertEqual(-10, hero.health)

    def test_battle_draw(self):
        enemy = Hero('abra', 1, 30, 30)
        hero = Hero('cadabra', 1, 30, 30)
        self.assertEqual('Draw', hero.battle(enemy))
        self.assertEqual(0, enemy.health)
        self.assertEqual(0, hero.health)

    def test_str_rep(self):
        self.assertEqual(str(self.hero),
                         "Hero abra: 12 lvl\n" \
                         "Health: 55.5\n" \
                         "Damage: 66.6\n"
                         )


if __name__ == '__main__':
    unittest.main()

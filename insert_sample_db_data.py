#!/usr/bin/env python
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "accountdemo.settings")

    snacks = ('Chips', 'Candy', 'Coke', 'Ice cream')
    first_names = ('Jeffrey', 'Chris', 'Jeff', 'John')
    last_names = ('Tucker', 'Fisher', 'Tucker', 'Doe')
    users = (
        {'user': 'Hercules', 'email': 'nobody@example.com'},
        {'user': 'Motoko', 'email': 'theman@example.com'},
        {'user': 'Azusa', 'email': 'lol@example.com'},
        {'user': 'mio32', 'email': '1337@example.com'},
        {'user': 'RiTsU_92', 'email': 'pro@example.com'},
        {'user': '1337', 'email': 'vim_god@example.com'},
        {'user': 'L33T', 'email': 'linux@example.com'},
        {'user': 'King', 'email': 'hjkl@example.com'},
        {'user': 'LinuxHero', 'email': 'bitcoin@example.com'},
        {'user': 'VimLover', 'email': 'litecoin@example.com'},
        {'user': 'vim', 'email': 'altcoin@example.com'},
    )

    def create_user(username, email, password):
        user = UserenaSignup.objects.create_user(username, email, password, True, False)
        user.first_name = first_names[random.randint(0, len(first_names) - 1)]
        user.last_name = last_names[random.randint(0, len(last_names) - 1)]
        user.save()
        profile = user.profile
        profile.favourite_snack = snacks[random.randint(0, len(snacks) - 1)]
        profile.save()

    import random
    from userena.models import UserenaSignup

    for user in users:
        create_user(user['user'], user['email'], 'lol')

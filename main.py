from structure import interface


def loop():
	chosen.data_deserialize()


if __name__ == '__main__':
	languages = interface.languages_list
	interface.print_languages(languages)
	chosen = interface.user_choice(languages)
	chosen.choose()

	while True:
		loop()

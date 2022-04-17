import json
from classes import Candidate


def candidates_preformat():
	"""Формирование списка кандидатов из файла с помещением их в форматированный список"""

	candidates_list = []

	with open("candidates.json", "r", encoding="utf-8") as file:
		candidates = json.load(file)

	for candidate in candidates:
		n = candidate.get("name")
		p = candidate.get("position")
		s = candidate.get("skills")

		new_format = Candidate(n, p, s)
		candidates_list.append(new_format)

	return candidates_list

import json


def all_candidates_loading():
	"""Формирование списка кандидатов из файла"""

	with open("candidates.json", "r", encoding="utf-8") as candidates:
		return json.load(candidates)


def candidates_format(candidates):
	"""Форматирование списка кандидатов для вывода на странице сайте"""
	candidates_list = "<pre>"

	for candidate in candidates:
		cand_name = candidate["name"]
		cand_position = candidate["position"]
		cand_skills = candidate["skills"]

		candidates_list += (
			f"Имя кандидата: {cand_name}<br/>"
			f"Позиция кандидата: {cand_position}<br/>"
			f"Навыки: {cand_skills}<br/>"
		)
		candidates_list += "<br/><pre>"

	return candidates_list


def candidate_by_id(candidates, cand_id):
	for candidate in candidates:
		if candidate["id"] == cand_id:
			return candidate


def candidate_by_skill(candidates, cand_skill):
	skill_list = []

	for candidate in candidates:
		candidates_skills = candidate["skills"].lower().split(", ")

		if cand_skill.lower() in candidates_skills:
			skill_list.append(candidate)

	return skill_list

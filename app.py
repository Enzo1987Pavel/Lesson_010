from flask import Flask

from funcs import all_candidates_loading, candidates_format, candidate_by_id, candidate_by_skill

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates_list = all_candidates_loading()
    return candidates_format(candidates_list)


@app.route("/candidates/<int:cand_id>")
def candidates_page(cand_id):
    candidates_list = all_candidates_loading()
    candidates = candidate_by_id(candidates_list, cand_id)

    result = f'<img src="{candidates["picture"]}">'

    return result + candidates_format([candidates])


@app.route("/skills/<skill>")
def skills_page(skill):
    candidates_list = all_candidates_loading()

    return candidates_format(candidate_by_skill(candidates_list, skill))


app.run()

from pyswip import Prolog
import time
import json


def prolog_query(query_string):
    prolog = Prolog()
    prolog.consult("knowledge.pl")
    results = []
    for res in prolog.query(query_string):
        results.append(res)

    return results


def ask_question(query_string):
    answers = prolog_query(query_string)
    return answers


def make_json(data):
    json_str = ""
    for c in data:
        if c == "'":
            json_str += '"'
            continue
        json_str += c
    return json_str


def say_answers(prefix, suffix, question_i, answers_i):
    for ansi in answers_i:
        ansi = make_json(str(ansi))
        obj = json.loads(str(ansi))
        print(obj[question_i])
        text = prefix + " " + obj[question_i] + " " + suffix
        print(">>>> ", text)


print(
    "Olá, estou aqui para conversar sobre a UFC de Itapajé. \
                O que deseja saber?"
)
flg = True
while flg:
    # Q/A
    print("\n\n")
    asked_question = str(input("O que deseja saber? ")).lower()

    if (
        "nome da universidade" in asked_question
        or "nome" in asked_question
    ):
        # Q: what is the name of the university?
        question = "UniversityName"
        query = "name(" + question + ")."
        answers = ask_question(query)
        say_answers("O nome da universidade é ", "", question, answers)

    elif (
        "introdução" in asked_question
        or "sobre a universidade" in asked_question
        or "sobre a UFC" in asked_question
    ):
        # Q: what is jahangirnagar university?
        question = "Introduction"
        query = "introduction('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif (
        "história da UFC" in asked_question
        or "história da Universidade" in asked_question
    ):
        # Q: history of jahangirnagar university.
        question = "History"
        query = "history('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("Breve história: ", "", question, answers)

    elif (
        "onde é a universidade" in asked_question
        or "situated" in asked_question
    ):
        # Q: where is jahangirnagar university?
        question = "Loction"
        query = "location('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif "área da universidade" in asked_question:
        # Q: where is jahangirnagar university?
        question = "Area"
        query = "area('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "a área da UFC é aproximadamente ", "", question, answers
        )

    elif (
        "atual" in asked_question
        or "agora" in asked_question
        or "hoje" in asked_question
    ) and ("vice coordenador" in asked_question or "vc" in asked_question):
        # Q: who is the current vice_chancellor of jahangirnagar university?
        question = "Vice_chancellor"
        query = "vice_chancellor('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "O atual vice coordenador do campus é ",
            "",
            question,
            answers,
        )

    elif (
        "number of faculties" in asked_question
        or "how many faculties" in asked_question
        and asked_question.find("faculty of") == -1
    ):
        # Q how many faculties are in jahangirnagr university
        question = "Number_of_faculties"
        query = "number_of_faculties('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "There are ", "faculties in jahangirnagar university", question, answers
        )

    elif (
        "number of departments" in asked_question
        or "how many departments" in asked_question
    ):
        # Q how many departments are in jahangirnagr university
        question = "Number_of_departments"
        query = "number_of_departments('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "There are ", "departments in jahangirnagar university", question, answers
        )

    elif (
        "number of institutes" in asked_question
        or "how many institutes" in asked_question
    ):
        # Q how many institutes are in jahangirnagr university
        question = "Number_of_institutes"
        query = "number_of_institutes('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "There are ", "institutes in jahangirnagar university", question, answers
        )

    elif (
        "quais cursos" in asked_question
        or "quais são os cursos" in asked_question
    ):
        # Q what are the faculties in jahangirnagar university
        question = "Facultiy"
        query = "faculties('jahangirnagar university', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "Existem três cursos na UFC de Itapajé, sendo eles ",
            "",
            question,
            answers,
        )

    elif (
        "names of the departments" in asked_question
        or "what are the departments" in asked_question
    ) and "under the faculty of" in asked_question:
        # Q what are the names departments in faculty of X?
        faculties = [
            "Análise e Desenvolvimento de Sistemas",
            "Ciência de Dados",
            "Segurança da Informação",
        ]
        id = -1
        for i in range(6):
            if faculties[i] in asked_question:
                id = i
                break
        if id != -1:
            print(faculties[id])
            question = "Departments"
            query = (
                "departments_under_faculty('jahangirnagar university', '"
                + faculties[id]
                + "',"
                + question
                + ")."
            )
            answers = ask_question(query)
            print(">>>>> ", "the departments under " + faculties[id] + " are, ")
            say_answers("", "", question, answers)

        else:
            print(">>>>> ", "me desculpe, não temos este curso no campus.")

    else:
        if asked_question != "-----------------":
            confirmation = str(
                input(
                    "Desculpe, isso não está no meu conhecimento. Posso ajudar em algo mais? "
                )
            ).lower()
            
            if "no" in confirmation or "nope" in confirmation or "stop" in confirmation:
                print(">>>>> ", "obrigado, espero que tenha sido proveitoso.")
                break
            else:
                continue

        time.sleep(2)

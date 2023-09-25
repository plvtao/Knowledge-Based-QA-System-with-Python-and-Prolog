name('Universidade Federal do Ceará').
breif_description('O Campus Jardins de Anita foi fundado em 2021 e oferece três cursos tecnólogos: Análise e Desenvolvimento de Sistemas, Ciência de Dados e Segurança da Informação.').
location('É localizado no município de Itapajé, e está localizado a 130km da capital.').
established('Universidade Federal do Ceará.', '2021').
first_vice_chancellor('Prof. Márcio Veras Corrêa').
current_vice_chancellor('Prof. Alberto Sampaio Lima').
history('O campus Jardins de Anita, planejado para iniciar suas atividades em 27 de setembro de 2021 pelo reitor da UFC Prof. Cândido Albuquerque, sob coordenação do Prof. Márcio Veras. Localizado na cidade de Itapajé, com pouco mais de 53 mil habitantes, e o nome do campus, Jardins de Anita, é uma homenagem à esposa do empresário José Maria de Sousa Melo, Anita Inará, nascida na Letônia, ambos falecidos.').
area('697.56 acres which is 2.8 square kilometres').
number_of_faculties('3').
faculty('Análise e Desenvolvimento de Sistemas').
faculty('Ciência de Dados').
faculty('Segurança da Informação').

faculties('Análise e Desenvolvimento de Sistemas, Ciência de Dados e Segurança da Informação').

departments('department of computer science and engineering, department of mathematics, department of physics, department of environmental science, department of chemistry, department of statistics, department of geological science, department of botany, department of zoology, department of biochemistry and molecular biology, department of microbiology, department of pharmacy, department of public health and informatics, department of biotechnology and genetic engineering, department of anthropology, department of economics, department of government and politics,\n\tdepartment of geography and environment, department of public administration, department of urban and regional planning, department of archaeology, department of bangla, department of drama and dramatics, department of english, department of fine arts, department of history, department of international relations, department of journalism and media studies, department of philosophy, department of accounting and information systems, department of finance and banking, department of marketing, department of management studies, department of accounting and information systems, department of finance and banking, department of marketing, department of management studies').

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
introduction(X, Y) :-
    name(X),
    breif_description(Y).
history(X, Y) :-
    name(X),
    history(Y).
location(X, Y) :-
    name(X),
    location(Y).
area(X, Y) :-
    name(X),
    area(Y).
first_vice_chancellor(X, Y) :-
    name(X),
    first_vice_chancellor(Y).
vice_chancellor(X, Y) :-
    name(X),
    current_vice_chancellor(Y).
number_of_faculties(X, Y) :-
    name(X),
    number_of_faculties(Y).
number_of_departments(X, Y) :-
    name(X),
    number_of_departments(Y).
number_of_institutes(X, Y) :-
    name(X),
    number_of_institutes(Y).

faculties(X, Y) :-
    name(X),
    faculties(Y).
departments(X, Y) :-
    name(X),
    departments(Y).
departments_under_faculty(X, Y, Z) :-
    name(X),
    faculty(Y),
    departments_under_faculty(Y, Z).
about_department_of_computer_science_and_engineering(X, Y) :-
    name(X),
    about_department_of_computer_science_and_engineering(Y).

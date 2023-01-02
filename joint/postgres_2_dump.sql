--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 14.6 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: d; Type: TABLE; Schema: public; Owner: stpatriarch
--

CREATE TABLE public.d (
    card_id integer NOT NULL,
    card_name text NOT NULL
);


ALTER TABLE public.d OWNER TO stpatriarch;

--
-- Name: d_card_id_seq; Type: SEQUENCE; Schema: public; Owner: stpatriarch
--

CREATE SEQUENCE public.d_card_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.d_card_id_seq OWNER TO stpatriarch;

--
-- Name: d_card_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: stpatriarch
--

ALTER SEQUENCE public.d_card_id_seq OWNED BY public.d.card_id;


--
-- Name: e; Type: TABLE; Schema: public; Owner: stpatriarch
--

CREATE TABLE public.e (
    card_id integer NOT NULL,
    card_name text NOT NULL
);


ALTER TABLE public.e OWNER TO stpatriarch;

--
-- Name: e_card_id_seq; Type: SEQUENCE; Schema: public; Owner: stpatriarch
--

CREATE SEQUENCE public.e_card_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.e_card_id_seq OWNER TO stpatriarch;

--
-- Name: e_card_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: stpatriarch
--

ALTER SEQUENCE public.e_card_id_seq OWNED BY public.e.card_id;


--
-- Name: l; Type: TABLE; Schema: public; Owner: stpatriarch
--

CREATE TABLE public.l (
    card_id integer NOT NULL,
    card_name text NOT NULL
);


ALTER TABLE public.l OWNER TO stpatriarch;

--
-- Name: l_card_id_seq; Type: SEQUENCE; Schema: public; Owner: stpatriarch
--

CREATE SEQUENCE public.l_card_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.l_card_id_seq OWNER TO stpatriarch;

--
-- Name: l_card_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: stpatriarch
--

ALTER SEQUENCE public.l_card_id_seq OWNED BY public.l.card_id;


--
-- Name: last_position; Type: TABLE; Schema: public; Owner: stpatriarch
--

CREATE TABLE public.last_position (
    card_id integer NOT NULL,
    card_name text NOT NULL
);


ALTER TABLE public.last_position OWNER TO stpatriarch;

--
-- Name: last_position_card_id_seq; Type: SEQUENCE; Schema: public; Owner: stpatriarch
--

CREATE SEQUENCE public.last_position_card_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.last_position_card_id_seq OWNER TO stpatriarch;

--
-- Name: last_position_card_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: stpatriarch
--

ALTER SEQUENCE public.last_position_card_id_seq OWNED BY public.last_position.card_id;


--
-- Name: players; Type: TABLE; Schema: public; Owner: stpatriarch
--

CREATE TABLE public.players (
    player_id integer NOT NULL,
    card_type text NOT NULL,
    p_1 real NOT NULL,
    p_2 real NOT NULL,
    p_3 real NOT NULL,
    p_4 real NOT NULL,
    p_5 real NOT NULL,
    p_6 real NOT NULL,
    p_7 real NOT NULL,
    p_8 real NOT NULL,
    p_9 real NOT NULL
);


ALTER TABLE public.players OWNER TO stpatriarch;

--
-- Name: players_player_id_seq; Type: SEQUENCE; Schema: public; Owner: stpatriarch
--

CREATE SEQUENCE public.players_player_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.players_player_id_seq OWNER TO stpatriarch;

--
-- Name: players_player_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: stpatriarch
--

ALTER SEQUENCE public.players_player_id_seq OWNED BY public.players.player_id;


--
-- Name: d card_id; Type: DEFAULT; Schema: public; Owner: stpatriarch
--

ALTER TABLE ONLY public.d ALTER COLUMN card_id SET DEFAULT nextval('public.d_card_id_seq'::regclass);


--
-- Name: e card_id; Type: DEFAULT; Schema: public; Owner: stpatriarch
--

ALTER TABLE ONLY public.e ALTER COLUMN card_id SET DEFAULT nextval('public.e_card_id_seq'::regclass);


--
-- Name: l card_id; Type: DEFAULT; Schema: public; Owner: stpatriarch
--

ALTER TABLE ONLY public.l ALTER COLUMN card_id SET DEFAULT nextval('public.l_card_id_seq'::regclass);


--
-- Name: last_position card_id; Type: DEFAULT; Schema: public; Owner: stpatriarch
--

ALTER TABLE ONLY public.last_position ALTER COLUMN card_id SET DEFAULT nextval('public.last_position_card_id_seq'::regclass);


--
-- Name: players player_id; Type: DEFAULT; Schema: public; Owner: stpatriarch
--

ALTER TABLE ONLY public.players ALTER COLUMN player_id SET DEFAULT nextval('public.players_player_id_seq'::regclass);


--
-- Data for Name: d; Type: TABLE DATA; Schema: public; Owner: stpatriarch
--

COPY public.d (card_id, card_name) FROM stdin;
1	AA
2	AK
3	KQ
4	QJ
5	J9
6	KK
7	AQ
8	KJ
9	QT
10	T9
11	QQ
12	AJ
13	KT
14	JT
15	JJ
16	AT
17	TT
18	99
19	88
20	77
\.


--
-- Data for Name: e; Type: TABLE DATA; Schema: public; Owner: stpatriarch
--

COPY public.e (card_id, card_name) FROM stdin;
1	AA
2	AK
3	KQ
4	JT
5	KK
6	AQ
7	KJ
8	J9
9	QQ
10	AJ
11	KT
12	J8
13	JJ
14	AT
15	K9
16	T9
17	TT
18	A9
19	QJ
20	T8
21	99
22	A8
23	QT
24	98
25	88
26	A7
27	Q9
28	77
29	A6
30	Q8
31	66
32	55
\.


--
-- Data for Name: l; Type: TABLE DATA; Schema: public; Owner: stpatriarch
--

COPY public.l (card_id, card_name) FROM stdin;
1	AA
2	AK
3	KQ
4	QJ
5	T7
6	KK
7	AQ
8	KJ
9	QT
10	98
11	QQ
12	AJ
13	KT
14	Q9
15	97
16	JJ
17	AT
18	K9
19	Q8
20	96
21	TT
22	A9
23	K8
24	JT
25	87
26	99
27	A8
28	K7
29	J9
30	86
31	88
32	A7
33	K6
34	J8
35	76
36	77
37	A6
38	K5
39	J7
40	75
41	66
42	A5
43	K4
44	T9
45	65
46	55
47	A4
48	K3
49	T8
50	44
51	A3
52	K2
53	33
54	A2
55	22
\.


--
-- Data for Name: last_position; Type: TABLE DATA; Schema: public; Owner: stpatriarch
--

COPY public.last_position (card_id, card_name) FROM stdin;
1	AA
2	AK
3	KQ
4	QJ
5	T7
6	KK
7	AQ
8	KJ
9	QT
10	98
11	QQ
12	AJ
13	KT
14	Q9
15	97
16	JJ
17	AT
18	K9
19	Q8
20	96
21	TT
22	A9
23	K8
24	JT
25	87
26	99
27	A8
28	K7
29	J9
30	86
31	88
32	A7
33	K6
34	J8
35	76
36	77
37	A6
38	K5
39	J7
40	75
41	66
42	A5
43	K4
44	T9
45	65
46	55
47	A4
48	K3
49	T8
50	44
51	A3
52	K2
53	33
54	A2
55	22
\.


--
-- Data for Name: players; Type: TABLE DATA; Schema: public; Owner: stpatriarch
--

COPY public.players (player_id, card_type, p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9) FROM stdin;
1	AA	85.4	73.4	63.9	55.8	48.9	43	38	33.6	29.8
2	KK	82.6	69.1	58.3	49.7	42.5	36.7	31.9	27.9	24.5
3	QQ	80.1	65.1	53.6	44.5	37.4	31.7	27.2	23.5	20.5
4	JJ	77.7	61.3	49.1	39.9	32.9	27.5	23.4	20.1	17.5
5	TT	75.2	57.7	45.1	35.9	29.2	24.2	20.4	17.5	15.3
6	99	72.3	53.7	41	32.2	25.8	21.3	18	15.5	13.7
7	88	69.4	50.1	37.4	28.9	23.1	19.1	16.2	14.1	12.6
8	77	66.5	46.6	34.2	26.2	20.9	17.3	14.8	13	11.7
9	66	63.6	43.3	31.3	23.8	19.1	15.9	13.8	12.2	11.1
10	55	60.7	40.2	28.6	21.7	17.4	14.7	12.8	11.5	10.4
11	44	57.4	36.8	25.8	19.8	16.1	13.8	12.2	11.1	10.2
12	33	54.2	33.7	23.6	18.2	15.1	13.1	11.8	10.8	10
13	22	50.9	30.8	21.5	16.8	14.2	12.6	11.5	10.6	9.9
14	AKs	67	50.7	41.4	35.4	31.6	27.7	24.9	22.7	20.6
15	AK	65.3	48.3	38.5	32.3	27.8	24.4	21.6	19.3	17.2
16	AQs	66.3	49.4	39.9	33.7	29.9	26	23.3	21	19.2
17	AQ	64.4	46.8	36.9	30.4	25.9	22.5	19.7	17.4	15.5
18	AJs	65.4	48.2	28.5	32.2	27.9	24.6	22	19.9	18.2
19	AJ	63.5	45.5	35.3	28.8	24.3	20.9	18.3	16.1	14.3
20	ATs	64.6	47.1	37.2	31	26.7	23.5	21	19	17.4
21	AT	62.7	44.3	34	27.5	23	19.7	17.2	15.1	13.3
22	A9s	62.8	44.5	34.5	28.3	24.1	21.1	18.8	16.9	15.4
23	A9	60.8	41.6	31	24	20.2	17.1	14.6	12.7	11.5
24	A8s	61.9	43.5	33.5	27.3	23.2	20.2	18	16.2	14.8
25	A8	59.9	40.4	29.9	23.5	19.2	16.1	13.8	11.9	10.5
26	A7s	61	42.4	32.4	26.4	22.4	19.5	17.4	15.6	14.3
27	A7	58.8	39.3	28.8	22.5	18.3	15.3	13.1	11.3	9.9
28	A6s	59.9	41.1	31.3	25.5	21.6	18.9	16.8	15.2	13.9
29	A6	57.7	37.9	27.5	21.4	17.4	14.6	12.5	10.9	9.5
30	A5s	59.9	41.5	31.7	26	22.2	19.5	17.4	15.8	14.5
31	A5	57.7	38.2	28	22	18	15.2	13.1	11.4	10.1
32	A4s	59	40.5	31	25.4	21.7	19	17.1	15.5	14.2
33	A4	56.7	37.2	27.2	21.3	17.5	14.8	12.7	12.1	9.9
34	A3s	58.2	39.7	30.2	24.8	21.2	18.6	16.7	15.2	14
35	A3	55.8	36.2	26.3	20.6	16.9	14.3	12.4	10.8	9.6
36	KQs	63.4	47.1	38.2	32.5	28.3	25.2	22.5	20.4	18.7
37	KQ	61.5	44.4	35.1	29.3	25.1	21.7	19.1	17	15.1
38	KJs	62.6	45.9	36.8	31.1	27	23.8	21.3	19.3	17.7
39	KJ	60.6	43.1	33.7	27.7	23.5	20.3	17.8	15.7	13.9
40	KTs	61.8	44.8	35.6	29.9	25.8	22.8	20.4	18.4	16.9
41	KT	59.7	41.9	32.4	26.4	22.2	19.1	16.7	14.7	13.1
42	QJs	60.3	44.2	35.7	30.2	26.3	23.2	20.7	18.8	17.2
43	QJ	58.1	41.4	32.5	26.9	22.8	19.8	17.3	15.3	13.7
44	QTs	59.4	43	34.6	29	25.2	22.2	20	18	16.6
45	QT	57.3	40.2	31.3	25.6	21.7	18.6	16.3	14.4	12.9
46	JTs	57.5	42	33.9	28.7	24.8	22	19.7	18	16.6
47	JT	55.3	39.1	30.7	25.4	21.5	18.5	16.3	14.5	13.1
48	J9s	55.7	39.4	31.2	26	22.3	19.6	17.5	15.8	14.5
49	J9	53.2	36.3	27.8	22.5	18.7	16	13.9	12.2	10.9
50	T9s	54	38.8	30.9	25.9	22.4	19.7	17.7	16.1	14.9
51	T9	51.5	35.6	27.6	22.5	18.9	16.2	14.2	12.6	11.3
52	98s	50.8	35.9	28.5	23.6	20.3	17.8	16	14.5	13.3
53	98	48.1	32.7	25	20.1	16.7	14.1	12.3	10.9	9.8
\.


--
-- Name: d_card_id_seq; Type: SEQUENCE SET; Schema: public; Owner: stpatriarch
--

SELECT pg_catalog.setval('public.d_card_id_seq', 20, true);


--
-- Name: e_card_id_seq; Type: SEQUENCE SET; Schema: public; Owner: stpatriarch
--

SELECT pg_catalog.setval('public.e_card_id_seq', 32, true);


--
-- Name: l_card_id_seq; Type: SEQUENCE SET; Schema: public; Owner: stpatriarch
--

SELECT pg_catalog.setval('public.l_card_id_seq', 55, true);


--
-- Name: last_position_card_id_seq; Type: SEQUENCE SET; Schema: public; Owner: stpatriarch
--

SELECT pg_catalog.setval('public.last_position_card_id_seq', 55, true);


--
-- Name: players_player_id_seq; Type: SEQUENCE SET; Schema: public; Owner: stpatriarch
--

SELECT pg_catalog.setval('public.players_player_id_seq', 53, true);


--
-- Name: d d_pkey; Type: CONSTRAINT; Schema: public; Owner: stpatriarch
--

ALTER TABLE ONLY public.d
    ADD CONSTRAINT d_pkey PRIMARY KEY (card_id);


--
-- Name: e e_pkey; Type: CONSTRAINT; Schema: public; Owner: stpatriarch
--

ALTER TABLE ONLY public.e
    ADD CONSTRAINT e_pkey PRIMARY KEY (card_id);


--
-- Name: l l_pkey; Type: CONSTRAINT; Schema: public; Owner: stpatriarch
--

ALTER TABLE ONLY public.l
    ADD CONSTRAINT l_pkey PRIMARY KEY (card_id);


--
-- Name: last_position last_position_pkey; Type: CONSTRAINT; Schema: public; Owner: stpatriarch
--

ALTER TABLE ONLY public.last_position
    ADD CONSTRAINT last_position_pkey PRIMARY KEY (card_id);


--
-- Name: players players_pkey; Type: CONSTRAINT; Schema: public; Owner: stpatriarch
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_pkey PRIMARY KEY (player_id);


--
-- PostgreSQL database dump complete
--


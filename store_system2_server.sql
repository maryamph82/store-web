--
-- PostgreSQL database cluster dump
--

-- Started on 2024-12-14 22:47:14

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE maryam;
ALTER ROLE maryam WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:J7gbG7kWJDUZCP7JFN4hiQ==$wypAxqVON3LqmQdUB7GRgwJ447UM0lgRIaEBaDvYmMU=:rM2rZqOXMee9JHwXC/e1ixT4f3B1+GfCuV11M0qnJK4=';
CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:2xOP0EuFxbu6umV3gBYgHA==$1rrCoh5adBGFHBBhFpGfsd9E7hWSyVLUNDBy/4+Ik/k=:ZSzcXYbAUSIJxhyMyDk+bMMwz+vx3DmhLnzB1znVF0Q=';






--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.18
-- Dumped by pg_dump version 13.18

-- Started on 2024-12-14 22:47:14

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

-- Completed on 2024-12-14 22:47:14

--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.18
-- Dumped by pg_dump version 13.18

-- Started on 2024-12-14 22:47:14

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

--
-- TOC entry 2 (class 3079 OID 16384)
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- TOC entry 2980 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


-- Completed on 2024-12-14 22:47:15

--
-- PostgreSQL database dump complete
--

--
-- Database "store_system" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.18
-- Dumped by pg_dump version 13.18

-- Started on 2024-12-14 22:47:15

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

--
-- TOC entry 3180 (class 1262 OID 16403)
-- Name: store_system; Type: DATABASE; Schema: -; Owner: maryam
--

CREATE DATABASE store_system WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';


ALTER DATABASE store_system OWNER TO maryam;

\connect store_system

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

--
-- TOC entry 724 (class 1247 OID 16648)
-- Name: gender; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.gender AS ENUM (
    'sport',
    'childish',
    'female',
    'male'
);


ALTER TYPE public.gender OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 221 (class 1259 OID 16569)
-- Name: bags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bags (
    bag_id integer NOT NULL,
    product_id integer
);


ALTER TABLE public.bags OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16567)
-- Name: bags_bag_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bags_bag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bags_bag_id_seq OWNER TO postgres;

--
-- TOC entry 3181 (class 0 OID 0)
-- Dependencies: 220
-- Name: bags_bag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bags_bag_id_seq OWNED BY public.bags.bag_id;


--
-- TOC entry 213 (class 1259 OID 16505)
-- Name: belts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.belts (
    belt_id integer NOT NULL,
    product_id integer,
    size text,
    width text,
    buckle_design text,
    hole_design text,
    type text
);


ALTER TABLE public.belts OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16503)
-- Name: belts_belt_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.belts_belt_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.belts_belt_id_seq OWNER TO postgres;

--
-- TOC entry 3182 (class 0 OID 0)
-- Dependencies: 212
-- Name: belts_belt_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.belts_belt_id_seq OWNED BY public.belts.belt_id;


--
-- TOC entry 201 (class 1259 OID 16409)
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    category_id integer NOT NULL,
    category_name text NOT NULL
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16407)
-- Name: categories_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categories_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_category_id_seq OWNER TO postgres;

--
-- TOC entry 3183 (class 0 OID 0)
-- Dependencies: 200
-- Name: categories_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categories_category_id_seq OWNED BY public.categories.category_id;


--
-- TOC entry 225 (class 1259 OID 16595)
-- Name: coats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.coats (
    coat_id integer NOT NULL,
    product_id integer,
    size text
);


ALTER TABLE public.coats OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16593)
-- Name: coats_coat_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.coats_coat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.coats_coat_id_seq OWNER TO postgres;

--
-- TOC entry 3184 (class 0 OID 0)
-- Dependencies: 224
-- Name: coats_coat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.coats_coat_id_seq OWNED BY public.coats.coat_id;


--
-- TOC entry 223 (class 1259 OID 16582)
-- Name: hats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hats (
    hat_id integer NOT NULL,
    product_id integer
);


ALTER TABLE public.hats OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16580)
-- Name: hats_hat_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.hats_hat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hats_hat_id_seq OWNER TO postgres;

--
-- TOC entry 3185 (class 0 OID 0)
-- Dependencies: 222
-- Name: hats_hat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.hats_hat_id_seq OWNED BY public.hats.hat_id;


--
-- TOC entry 229 (class 1259 OID 16627)
-- Name: hoodies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hoodies (
    hoodie_id integer NOT NULL,
    product_id integer,
    size text,
    with_hood boolean
);


ALTER TABLE public.hoodies OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 16625)
-- Name: hoodies_hoodie_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.hoodies_hoodie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hoodies_hoodie_id_seq OWNER TO postgres;

--
-- TOC entry 3186 (class 0 OID 0)
-- Dependencies: 228
-- Name: hoodies_hoodie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.hoodies_hoodie_id_seq OWNED BY public.hoodies.hoodie_id;


--
-- TOC entry 207 (class 1259 OID 16452)
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    order_id integer NOT NULL,
    product_id integer,
    user_id integer,
    order_date date,
    order_status text,
    payment_method text
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16450)
-- Name: orders_order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_order_id_seq OWNER TO postgres;

--
-- TOC entry 3187 (class 0 OID 0)
-- Dependencies: 206
-- Name: orders_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;


--
-- TOC entry 209 (class 1259 OID 16473)
-- Name: pants; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pants (
    pant_id integer NOT NULL,
    product_id integer,
    size text,
    type text
);


ALTER TABLE public.pants OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 16471)
-- Name: pants_pant_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pants_pant_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pants_pant_id_seq OWNER TO postgres;

--
-- TOC entry 3188 (class 0 OID 0)
-- Dependencies: 208
-- Name: pants_pant_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pants_pant_id_seq OWNED BY public.pants.pant_id;


--
-- TOC entry 205 (class 1259 OID 16431)
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    product_id integer NOT NULL,
    name text,
    color text,
    quantity integer,
    user_id integer,
    category_id integer,
    gender public.gender,
    brand text,
    price numeric,
    material text
);


ALTER TABLE public.products OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16429)
-- Name: products_product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_product_id_seq OWNER TO postgres;

--
-- TOC entry 3189 (class 0 OID 0)
-- Dependencies: 204
-- Name: products_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_product_id_seq OWNED BY public.products.product_id;


--
-- TOC entry 217 (class 1259 OID 16537)
-- Name: scarves; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scarves (
    scarf_id integer NOT NULL,
    product_id integer,
    season text,
    pattern text
);


ALTER TABLE public.scarves OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16535)
-- Name: scarves_scarf_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scarves_scarf_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.scarves_scarf_id_seq OWNER TO postgres;

--
-- TOC entry 3190 (class 0 OID 0)
-- Dependencies: 216
-- Name: scarves_scarf_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scarves_scarf_id_seq OWNED BY public.scarves.scarf_id;


--
-- TOC entry 211 (class 1259 OID 16489)
-- Name: shoes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shoes (
    shoe_id integer NOT NULL,
    product_id integer,
    size text,
    ankle_type text
);


ALTER TABLE public.shoes OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16487)
-- Name: shoes_shoe_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shoes_shoe_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shoes_shoe_id_seq OWNER TO postgres;

--
-- TOC entry 3191 (class 0 OID 0)
-- Dependencies: 210
-- Name: shoes_shoe_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.shoes_shoe_id_seq OWNED BY public.shoes.shoe_id;


--
-- TOC entry 215 (class 1259 OID 16521)
-- Name: skirts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.skirts (
    skirt_id integer NOT NULL,
    product_id integer,
    size text,
    pattern text,
    length text
);


ALTER TABLE public.skirts OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16519)
-- Name: skirts_skirt_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.skirts_skirt_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.skirts_skirt_id_seq OWNER TO postgres;

--
-- TOC entry 3192 (class 0 OID 0)
-- Dependencies: 214
-- Name: skirts_skirt_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.skirts_skirt_id_seq OWNED BY public.skirts.skirt_id;


--
-- TOC entry 219 (class 1259 OID 16553)
-- Name: socks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socks (
    sock_id integer NOT NULL,
    product_id integer,
    pattern text,
    size text
);


ALTER TABLE public.socks OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16551)
-- Name: socks_sock_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socks_sock_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socks_sock_id_seq OWNER TO postgres;

--
-- TOC entry 3193 (class 0 OID 0)
-- Dependencies: 218
-- Name: socks_sock_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socks_sock_id_seq OWNED BY public.socks.sock_id;


--
-- TOC entry 227 (class 1259 OID 16611)
-- Name: tshirts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tshirts (
    tshirt_id integer NOT NULL,
    product_id integer,
    size text
);


ALTER TABLE public.tshirts OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16609)
-- Name: tshirts_tshirt_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tshirts_tshirt_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tshirts_tshirt_id_seq OWNER TO postgres;

--
-- TOC entry 3194 (class 0 OID 0)
-- Dependencies: 226
-- Name: tshirts_tshirt_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tshirts_tshirt_id_seq OWNED BY public.tshirts.tshirt_id;


--
-- TOC entry 203 (class 1259 OID 16420)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    postal_code text,
    address text,
    first_name text,
    last_name text,
    national_code text,
    phone_number text,
    birth_date date,
    user_type text
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16418)
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO postgres;

--
-- TOC entry 3195 (class 0 OID 0)
-- Dependencies: 202
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- TOC entry 2960 (class 2604 OID 16572)
-- Name: bags bag_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bags ALTER COLUMN bag_id SET DEFAULT nextval('public.bags_bag_id_seq'::regclass);


--
-- TOC entry 2956 (class 2604 OID 16508)
-- Name: belts belt_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.belts ALTER COLUMN belt_id SET DEFAULT nextval('public.belts_belt_id_seq'::regclass);


--
-- TOC entry 2950 (class 2604 OID 16412)
-- Name: categories category_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories ALTER COLUMN category_id SET DEFAULT nextval('public.categories_category_id_seq'::regclass);


--
-- TOC entry 2962 (class 2604 OID 16598)
-- Name: coats coat_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coats ALTER COLUMN coat_id SET DEFAULT nextval('public.coats_coat_id_seq'::regclass);


--
-- TOC entry 2961 (class 2604 OID 16585)
-- Name: hats hat_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hats ALTER COLUMN hat_id SET DEFAULT nextval('public.hats_hat_id_seq'::regclass);


--
-- TOC entry 2964 (class 2604 OID 16630)
-- Name: hoodies hoodie_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hoodies ALTER COLUMN hoodie_id SET DEFAULT nextval('public.hoodies_hoodie_id_seq'::regclass);


--
-- TOC entry 2953 (class 2604 OID 16455)
-- Name: orders order_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);


--
-- TOC entry 2954 (class 2604 OID 16476)
-- Name: pants pant_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pants ALTER COLUMN pant_id SET DEFAULT nextval('public.pants_pant_id_seq'::regclass);


--
-- TOC entry 2952 (class 2604 OID 16434)
-- Name: products product_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products ALTER COLUMN product_id SET DEFAULT nextval('public.products_product_id_seq'::regclass);


--
-- TOC entry 2958 (class 2604 OID 16540)
-- Name: scarves scarf_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scarves ALTER COLUMN scarf_id SET DEFAULT nextval('public.scarves_scarf_id_seq'::regclass);


--
-- TOC entry 2955 (class 2604 OID 16492)
-- Name: shoes shoe_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shoes ALTER COLUMN shoe_id SET DEFAULT nextval('public.shoes_shoe_id_seq'::regclass);


--
-- TOC entry 2957 (class 2604 OID 16524)
-- Name: skirts skirt_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skirts ALTER COLUMN skirt_id SET DEFAULT nextval('public.skirts_skirt_id_seq'::regclass);


--
-- TOC entry 2959 (class 2604 OID 16556)
-- Name: socks sock_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socks ALTER COLUMN sock_id SET DEFAULT nextval('public.socks_sock_id_seq'::regclass);


--
-- TOC entry 2963 (class 2604 OID 16614)
-- Name: tshirts tshirt_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tshirts ALTER COLUMN tshirt_id SET DEFAULT nextval('public.tshirts_tshirt_id_seq'::regclass);


--
-- TOC entry 2951 (class 2604 OID 16423)
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- TOC entry 3166 (class 0 OID 16569)
-- Dependencies: 221
-- Data for Name: bags; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bags (bag_id, product_id) FROM stdin;
\.


--
-- TOC entry 3158 (class 0 OID 16505)
-- Dependencies: 213
-- Data for Name: belts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.belts (belt_id, product_id, size, width, buckle_design, hole_design, type) FROM stdin;
\.


--
-- TOC entry 3146 (class 0 OID 16409)
-- Dependencies: 201
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categories (category_id, category_name) FROM stdin;
\.


--
-- TOC entry 3170 (class 0 OID 16595)
-- Dependencies: 225
-- Data for Name: coats; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.coats (coat_id, product_id, size) FROM stdin;
\.


--
-- TOC entry 3168 (class 0 OID 16582)
-- Dependencies: 223
-- Data for Name: hats; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hats (hat_id, product_id) FROM stdin;
\.


--
-- TOC entry 3174 (class 0 OID 16627)
-- Dependencies: 229
-- Data for Name: hoodies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hoodies (hoodie_id, product_id, size, with_hood) FROM stdin;
\.


--
-- TOC entry 3152 (class 0 OID 16452)
-- Dependencies: 207
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (order_id, product_id, user_id, order_date, order_status, payment_method) FROM stdin;
\.


--
-- TOC entry 3154 (class 0 OID 16473)
-- Dependencies: 209
-- Data for Name: pants; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pants (pant_id, product_id, size, type) FROM stdin;
\.


--
-- TOC entry 3150 (class 0 OID 16431)
-- Dependencies: 205
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products (product_id, name, color, quantity, user_id, category_id, gender, brand, price, material) FROM stdin;
\.


--
-- TOC entry 3162 (class 0 OID 16537)
-- Dependencies: 217
-- Data for Name: scarves; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.scarves (scarf_id, product_id, season, pattern) FROM stdin;
\.


--
-- TOC entry 3156 (class 0 OID 16489)
-- Dependencies: 211
-- Data for Name: shoes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shoes (shoe_id, product_id, size, ankle_type) FROM stdin;
\.


--
-- TOC entry 3160 (class 0 OID 16521)
-- Dependencies: 215
-- Data for Name: skirts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.skirts (skirt_id, product_id, size, pattern, length) FROM stdin;
\.


--
-- TOC entry 3164 (class 0 OID 16553)
-- Dependencies: 219
-- Data for Name: socks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socks (sock_id, product_id, pattern, size) FROM stdin;
\.


--
-- TOC entry 3172 (class 0 OID 16611)
-- Dependencies: 227
-- Data for Name: tshirts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tshirts (tshirt_id, product_id, size) FROM stdin;
\.


--
-- TOC entry 3148 (class 0 OID 16420)
-- Dependencies: 203
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (user_id, postal_code, address, first_name, last_name, national_code, phone_number, birth_date, user_type) FROM stdin;
\.


--
-- TOC entry 3196 (class 0 OID 0)
-- Dependencies: 220
-- Name: bags_bag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bags_bag_id_seq', 1, false);


--
-- TOC entry 3197 (class 0 OID 0)
-- Dependencies: 212
-- Name: belts_belt_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.belts_belt_id_seq', 1, false);


--
-- TOC entry 3198 (class 0 OID 0)
-- Dependencies: 200
-- Name: categories_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_category_id_seq', 1, false);


--
-- TOC entry 3199 (class 0 OID 0)
-- Dependencies: 224
-- Name: coats_coat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.coats_coat_id_seq', 1, false);


--
-- TOC entry 3200 (class 0 OID 0)
-- Dependencies: 222
-- Name: hats_hat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hats_hat_id_seq', 1, false);


--
-- TOC entry 3201 (class 0 OID 0)
-- Dependencies: 228
-- Name: hoodies_hoodie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hoodies_hoodie_id_seq', 1, false);


--
-- TOC entry 3202 (class 0 OID 0)
-- Dependencies: 206
-- Name: orders_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_order_id_seq', 1, false);


--
-- TOC entry 3203 (class 0 OID 0)
-- Dependencies: 208
-- Name: pants_pant_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pants_pant_id_seq', 1, false);


--
-- TOC entry 3204 (class 0 OID 0)
-- Dependencies: 204
-- Name: products_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_product_id_seq', 1, false);


--
-- TOC entry 3205 (class 0 OID 0)
-- Dependencies: 216
-- Name: scarves_scarf_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scarves_scarf_id_seq', 1, false);


--
-- TOC entry 3206 (class 0 OID 0)
-- Dependencies: 210
-- Name: shoes_shoe_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shoes_shoe_id_seq', 1, false);


--
-- TOC entry 3207 (class 0 OID 0)
-- Dependencies: 214
-- Name: skirts_skirt_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.skirts_skirt_id_seq', 1, false);


--
-- TOC entry 3208 (class 0 OID 0)
-- Dependencies: 218
-- Name: socks_sock_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socks_sock_id_seq', 1, false);


--
-- TOC entry 3209 (class 0 OID 0)
-- Dependencies: 226
-- Name: tshirts_tshirt_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tshirts_tshirt_id_seq', 1, false);


--
-- TOC entry 3210 (class 0 OID 0)
-- Dependencies: 202
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 1, false);


--
-- TOC entry 2991 (class 2606 OID 16574)
-- Name: bags bags_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bags
    ADD CONSTRAINT bags_pkey PRIMARY KEY (bag_id);


--
-- TOC entry 2983 (class 2606 OID 16513)
-- Name: belts belts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.belts
    ADD CONSTRAINT belts_pkey PRIMARY KEY (belt_id);


--
-- TOC entry 2966 (class 2606 OID 16417)
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category_id);


--
-- TOC entry 2995 (class 2606 OID 16603)
-- Name: coats coats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coats
    ADD CONSTRAINT coats_pkey PRIMARY KEY (coat_id);


--
-- TOC entry 2993 (class 2606 OID 16587)
-- Name: hats hats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hats
    ADD CONSTRAINT hats_pkey PRIMARY KEY (hat_id);


--
-- TOC entry 2999 (class 2606 OID 16635)
-- Name: hoodies hoodies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hoodies
    ADD CONSTRAINT hoodies_pkey PRIMARY KEY (hoodie_id);


--
-- TOC entry 2977 (class 2606 OID 16460)
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);


--
-- TOC entry 2979 (class 2606 OID 16481)
-- Name: pants pants_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pants
    ADD CONSTRAINT pants_pkey PRIMARY KEY (pant_id);


--
-- TOC entry 2974 (class 2606 OID 16439)
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);


--
-- TOC entry 2987 (class 2606 OID 16545)
-- Name: scarves scarves_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scarves
    ADD CONSTRAINT scarves_pkey PRIMARY KEY (scarf_id);


--
-- TOC entry 2981 (class 2606 OID 16497)
-- Name: shoes shoes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shoes
    ADD CONSTRAINT shoes_pkey PRIMARY KEY (shoe_id);


--
-- TOC entry 2985 (class 2606 OID 16529)
-- Name: skirts skirts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skirts
    ADD CONSTRAINT skirts_pkey PRIMARY KEY (skirt_id);


--
-- TOC entry 2989 (class 2606 OID 16561)
-- Name: socks socks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socks
    ADD CONSTRAINT socks_pkey PRIMARY KEY (sock_id);


--
-- TOC entry 2997 (class 2606 OID 16619)
-- Name: tshirts tshirts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tshirts
    ADD CONSTRAINT tshirts_pkey PRIMARY KEY (tshirt_id);


--
-- TOC entry 2970 (class 2606 OID 16428)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- TOC entry 2975 (class 1259 OID 16646)
-- Name: idx_orders_userid_date_status; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_orders_userid_date_status ON public.orders USING btree (user_id, order_date, order_status);


--
-- TOC entry 2971 (class 1259 OID 16643)
-- Name: idx_productid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_productid ON public.products USING btree (product_id);


--
-- TOC entry 2972 (class 1259 OID 16657)
-- Name: idx_products_userid_categoryid_gender_brand_price; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_products_userid_categoryid_gender_brand_price ON public.products USING btree (user_id, category_id, gender, brand, price);


--
-- TOC entry 2967 (class 1259 OID 16644)
-- Name: idx_users_firstname_lastname_nationalcode; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_users_firstname_lastname_nationalcode ON public.users USING btree (first_name, last_name, national_code);


--
-- TOC entry 2968 (class 1259 OID 16645)
-- Name: idx_users_postalcode; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_users_postalcode ON public.users USING btree (postal_code);


--
-- TOC entry 3010 (class 2606 OID 16575)
-- Name: bags bags_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bags
    ADD CONSTRAINT bags_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- TOC entry 3006 (class 2606 OID 16514)
-- Name: belts belts_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.belts
    ADD CONSTRAINT belts_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- TOC entry 3012 (class 2606 OID 16604)
-- Name: coats coats_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coats
    ADD CONSTRAINT coats_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- TOC entry 3011 (class 2606 OID 16588)
-- Name: hats hats_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hats
    ADD CONSTRAINT hats_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- TOC entry 3014 (class 2606 OID 16636)
-- Name: hoodies hoodies_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hoodies
    ADD CONSTRAINT hoodies_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- TOC entry 3002 (class 2606 OID 16461)
-- Name: orders orders_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- TOC entry 3003 (class 2606 OID 16466)
-- Name: orders orders_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- TOC entry 3004 (class 2606 OID 16482)
-- Name: pants pants_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pants
    ADD CONSTRAINT pants_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- TOC entry 3001 (class 2606 OID 16445)
-- Name: products products_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(category_id);


--
-- TOC entry 3000 (class 2606 OID 16440)
-- Name: products products_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- TOC entry 3008 (class 2606 OID 16546)
-- Name: scarves scarves_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scarves
    ADD CONSTRAINT scarves_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- TOC entry 3005 (class 2606 OID 16498)
-- Name: shoes shoes_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shoes
    ADD CONSTRAINT shoes_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- TOC entry 3007 (class 2606 OID 16530)
-- Name: skirts skirts_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skirts
    ADD CONSTRAINT skirts_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- TOC entry 3009 (class 2606 OID 16562)
-- Name: socks socks_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socks
    ADD CONSTRAINT socks_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- TOC entry 3013 (class 2606 OID 16620)
-- Name: tshirts tshirts_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tshirts
    ADD CONSTRAINT tshirts_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


-- Completed on 2024-12-14 22:47:15

--
-- PostgreSQL database dump complete
--

-- Completed on 2024-12-14 22:47:15

--
-- PostgreSQL database cluster dump complete
--


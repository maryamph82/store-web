PGDMP         )                |            store_system    13.18    13.18 �    i           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            j           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            k           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            l           1262    16403    store_system    DATABASE     p   CREATE DATABASE store_system WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE store_system;
                maryam    false            �           1247    16648    gender    TYPE     ]   CREATE TYPE public.gender AS ENUM (
    'sport',
    'childish',
    'female',
    'male'
);
    DROP TYPE public.gender;
       public          postgres    false            �            1259    16569    bags    TABLE     h   CREATE TABLE public.bags (
    bag_id integer NOT NULL,
    product_id integer,
    description text
);
    DROP TABLE public.bags;
       public         heap    postgres    false            �            1259    16567    bags_bag_id_seq    SEQUENCE     �   CREATE SEQUENCE public.bags_bag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.bags_bag_id_seq;
       public          postgres    false    221            m           0    0    bags_bag_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.bags_bag_id_seq OWNED BY public.bags.bag_id;
          public          postgres    false    220            �            1259    16505    belts    TABLE     j   CREATE TABLE public.belts (
    belt_id integer NOT NULL,
    product_id integer,
    description text
);
    DROP TABLE public.belts;
       public         heap    postgres    false            �            1259    16503    belts_belt_id_seq    SEQUENCE     �   CREATE SEQUENCE public.belts_belt_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.belts_belt_id_seq;
       public          postgres    false    213            n           0    0    belts_belt_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.belts_belt_id_seq OWNED BY public.belts.belt_id;
          public          postgres    false    212            �            1259    16409 
   categories    TABLE     f   CREATE TABLE public.categories (
    category_id integer NOT NULL,
    category_name text NOT NULL
);
    DROP TABLE public.categories;
       public         heap    postgres    false            �            1259    16407    categories_category_id_seq    SEQUENCE     �   CREATE SEQUENCE public.categories_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.categories_category_id_seq;
       public          postgres    false    201            o           0    0    categories_category_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.categories_category_id_seq OWNED BY public.categories.category_id;
          public          postgres    false    200            �            1259    16595    coats    TABLE     y   CREATE TABLE public.coats (
    coat_id integer NOT NULL,
    product_id integer,
    size text,
    description text
);
    DROP TABLE public.coats;
       public         heap    postgres    false            �            1259    16593    coats_coat_id_seq    SEQUENCE     �   CREATE SEQUENCE public.coats_coat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.coats_coat_id_seq;
       public          postgres    false    225            p           0    0    coats_coat_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.coats_coat_id_seq OWNED BY public.coats.coat_id;
          public          postgres    false    224            �            1259    16582    hats    TABLE     h   CREATE TABLE public.hats (
    hat_id integer NOT NULL,
    product_id integer,
    description text
);
    DROP TABLE public.hats;
       public         heap    postgres    false            �            1259    16580    hats_hat_id_seq    SEQUENCE     �   CREATE SEQUENCE public.hats_hat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.hats_hat_id_seq;
       public          postgres    false    223            q           0    0    hats_hat_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.hats_hat_id_seq OWNED BY public.hats.hat_id;
          public          postgres    false    222            �            1259    16627    hoodies    TABLE     �   CREATE TABLE public.hoodies (
    hoodie_id integer NOT NULL,
    product_id integer,
    size text,
    with_hood boolean,
    description text
);
    DROP TABLE public.hoodies;
       public         heap    postgres    false            �            1259    16625    hoodies_hoodie_id_seq    SEQUENCE     �   CREATE SEQUENCE public.hoodies_hoodie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.hoodies_hoodie_id_seq;
       public          postgres    false    229            r           0    0    hoodies_hoodie_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.hoodies_hoodie_id_seq OWNED BY public.hoodies.hoodie_id;
          public          postgres    false    228            �            1259    16452    orders    TABLE     �   CREATE TABLE public.orders (
    order_id integer NOT NULL,
    product_id integer,
    user_id integer,
    order_date date,
    payment_method text,
    order_status boolean,
    quantity integer
);
    DROP TABLE public.orders;
       public         heap    postgres    false            �            1259    16450    orders_order_id_seq    SEQUENCE     �   CREATE SEQUENCE public.orders_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.orders_order_id_seq;
       public          postgres    false    207            s           0    0    orders_order_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;
          public          postgres    false    206            �            1259    16473    pants    TABLE     y   CREATE TABLE public.pants (
    pant_id integer NOT NULL,
    product_id integer,
    size text,
    description text
);
    DROP TABLE public.pants;
       public         heap    postgres    false            �            1259    16471    pants_pant_id_seq    SEQUENCE     �   CREATE SEQUENCE public.pants_pant_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.pants_pant_id_seq;
       public          postgres    false    209            t           0    0    pants_pant_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.pants_pant_id_seq OWNED BY public.pants.pant_id;
          public          postgres    false    208            �            1259    16431    products    TABLE       CREATE TABLE public.products (
    product_id integer NOT NULL,
    name text,
    color text,
    quantity integer,
    user_id integer,
    category_id integer,
    gender public.gender,
    brand text,
    material text,
    date date,
    picture bytea,
    price real
);
    DROP TABLE public.products;
       public         heap    postgres    false    724            �            1259    16429    products_product_id_seq    SEQUENCE     �   CREATE SEQUENCE public.products_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.products_product_id_seq;
       public          postgres    false    205            u           0    0    products_product_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.products_product_id_seq OWNED BY public.products.product_id;
          public          postgres    false    204            �            1259    16537    scarves    TABLE     m   CREATE TABLE public.scarves (
    scarf_id integer NOT NULL,
    product_id integer,
    description text
);
    DROP TABLE public.scarves;
       public         heap    postgres    false            �            1259    16535    scarves_scarf_id_seq    SEQUENCE     �   CREATE SEQUENCE public.scarves_scarf_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.scarves_scarf_id_seq;
       public          postgres    false    217            v           0    0    scarves_scarf_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.scarves_scarf_id_seq OWNED BY public.scarves.scarf_id;
          public          postgres    false    216            �            1259    16489    shoes    TABLE     y   CREATE TABLE public.shoes (
    shoe_id integer NOT NULL,
    product_id integer,
    size text,
    description text
);
    DROP TABLE public.shoes;
       public         heap    postgres    false            �            1259    16487    shoes_shoe_id_seq    SEQUENCE     �   CREATE SEQUENCE public.shoes_shoe_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.shoes_shoe_id_seq;
       public          postgres    false    211            w           0    0    shoes_shoe_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.shoes_shoe_id_seq OWNED BY public.shoes.shoe_id;
          public          postgres    false    210            �            1259    16521    skirts    TABLE     {   CREATE TABLE public.skirts (
    skirt_id integer NOT NULL,
    product_id integer,
    size text,
    description text
);
    DROP TABLE public.skirts;
       public         heap    postgres    false            �            1259    16519    skirts_skirt_id_seq    SEQUENCE     �   CREATE SEQUENCE public.skirts_skirt_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.skirts_skirt_id_seq;
       public          postgres    false    215            x           0    0    skirts_skirt_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.skirts_skirt_id_seq OWNED BY public.skirts.skirt_id;
          public          postgres    false    214            �            1259    16553    socks    TABLE     j   CREATE TABLE public.socks (
    sock_id integer NOT NULL,
    product_id integer,
    description text
);
    DROP TABLE public.socks;
       public         heap    postgres    false            �            1259    16551    socks_sock_id_seq    SEQUENCE     �   CREATE SEQUENCE public.socks_sock_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.socks_sock_id_seq;
       public          postgres    false    219            y           0    0    socks_sock_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.socks_sock_id_seq OWNED BY public.socks.sock_id;
          public          postgres    false    218            �            1259    16611    tshirts    TABLE     }   CREATE TABLE public.tshirts (
    tshirt_id integer NOT NULL,
    product_id integer,
    size text,
    description text
);
    DROP TABLE public.tshirts;
       public         heap    postgres    false            �            1259    16609    tshirts_tshirt_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tshirts_tshirt_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.tshirts_tshirt_id_seq;
       public          postgres    false    227            z           0    0    tshirts_tshirt_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.tshirts_tshirt_id_seq OWNED BY public.tshirts.tshirt_id;
          public          postgres    false    226            �            1259    16420    users    TABLE       CREATE TABLE public.users (
    user_id integer NOT NULL,
    postal_code text,
    address text,
    first_name text,
    last_name text,
    national_code text,
    phone_number text,
    birth_date date,
    user_type text,
    password text NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    16418    users_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.users_user_id_seq;
       public          postgres    false    203            {           0    0    users_user_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;
          public          postgres    false    202            �           2604    16572    bags bag_id    DEFAULT     j   ALTER TABLE ONLY public.bags ALTER COLUMN bag_id SET DEFAULT nextval('public.bags_bag_id_seq'::regclass);
 :   ALTER TABLE public.bags ALTER COLUMN bag_id DROP DEFAULT;
       public          postgres    false    220    221    221            �           2604    16508    belts belt_id    DEFAULT     n   ALTER TABLE ONLY public.belts ALTER COLUMN belt_id SET DEFAULT nextval('public.belts_belt_id_seq'::regclass);
 <   ALTER TABLE public.belts ALTER COLUMN belt_id DROP DEFAULT;
       public          postgres    false    213    212    213            �           2604    16412    categories category_id    DEFAULT     �   ALTER TABLE ONLY public.categories ALTER COLUMN category_id SET DEFAULT nextval('public.categories_category_id_seq'::regclass);
 E   ALTER TABLE public.categories ALTER COLUMN category_id DROP DEFAULT;
       public          postgres    false    200    201    201            �           2604    16598    coats coat_id    DEFAULT     n   ALTER TABLE ONLY public.coats ALTER COLUMN coat_id SET DEFAULT nextval('public.coats_coat_id_seq'::regclass);
 <   ALTER TABLE public.coats ALTER COLUMN coat_id DROP DEFAULT;
       public          postgres    false    225    224    225            �           2604    16585    hats hat_id    DEFAULT     j   ALTER TABLE ONLY public.hats ALTER COLUMN hat_id SET DEFAULT nextval('public.hats_hat_id_seq'::regclass);
 :   ALTER TABLE public.hats ALTER COLUMN hat_id DROP DEFAULT;
       public          postgres    false    223    222    223            �           2604    16630    hoodies hoodie_id    DEFAULT     v   ALTER TABLE ONLY public.hoodies ALTER COLUMN hoodie_id SET DEFAULT nextval('public.hoodies_hoodie_id_seq'::regclass);
 @   ALTER TABLE public.hoodies ALTER COLUMN hoodie_id DROP DEFAULT;
       public          postgres    false    228    229    229            �           2604    16455    orders order_id    DEFAULT     r   ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);
 >   ALTER TABLE public.orders ALTER COLUMN order_id DROP DEFAULT;
       public          postgres    false    207    206    207            �           2604    16476    pants pant_id    DEFAULT     n   ALTER TABLE ONLY public.pants ALTER COLUMN pant_id SET DEFAULT nextval('public.pants_pant_id_seq'::regclass);
 <   ALTER TABLE public.pants ALTER COLUMN pant_id DROP DEFAULT;
       public          postgres    false    208    209    209            �           2604    16434    products product_id    DEFAULT     z   ALTER TABLE ONLY public.products ALTER COLUMN product_id SET DEFAULT nextval('public.products_product_id_seq'::regclass);
 B   ALTER TABLE public.products ALTER COLUMN product_id DROP DEFAULT;
       public          postgres    false    205    204    205            �           2604    16540    scarves scarf_id    DEFAULT     t   ALTER TABLE ONLY public.scarves ALTER COLUMN scarf_id SET DEFAULT nextval('public.scarves_scarf_id_seq'::regclass);
 ?   ALTER TABLE public.scarves ALTER COLUMN scarf_id DROP DEFAULT;
       public          postgres    false    216    217    217            �           2604    16492    shoes shoe_id    DEFAULT     n   ALTER TABLE ONLY public.shoes ALTER COLUMN shoe_id SET DEFAULT nextval('public.shoes_shoe_id_seq'::regclass);
 <   ALTER TABLE public.shoes ALTER COLUMN shoe_id DROP DEFAULT;
       public          postgres    false    210    211    211            �           2604    16524    skirts skirt_id    DEFAULT     r   ALTER TABLE ONLY public.skirts ALTER COLUMN skirt_id SET DEFAULT nextval('public.skirts_skirt_id_seq'::regclass);
 >   ALTER TABLE public.skirts ALTER COLUMN skirt_id DROP DEFAULT;
       public          postgres    false    214    215    215            �           2604    16556    socks sock_id    DEFAULT     n   ALTER TABLE ONLY public.socks ALTER COLUMN sock_id SET DEFAULT nextval('public.socks_sock_id_seq'::regclass);
 <   ALTER TABLE public.socks ALTER COLUMN sock_id DROP DEFAULT;
       public          postgres    false    219    218    219            �           2604    16614    tshirts tshirt_id    DEFAULT     v   ALTER TABLE ONLY public.tshirts ALTER COLUMN tshirt_id SET DEFAULT nextval('public.tshirts_tshirt_id_seq'::regclass);
 @   ALTER TABLE public.tshirts ALTER COLUMN tshirt_id DROP DEFAULT;
       public          postgres    false    227    226    227            �           2604    16423    users user_id    DEFAULT     n   ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);
 <   ALTER TABLE public.users ALTER COLUMN user_id DROP DEFAULT;
       public          postgres    false    202    203    203            ^          0    16569    bags 
   TABLE DATA           ?   COPY public.bags (bag_id, product_id, description) FROM stdin;
    public          postgres    false    221   ��       V          0    16505    belts 
   TABLE DATA           A   COPY public.belts (belt_id, product_id, description) FROM stdin;
    public          postgres    false    213   ҏ       J          0    16409 
   categories 
   TABLE DATA           @   COPY public.categories (category_id, category_name) FROM stdin;
    public          postgres    false    201   �       b          0    16595    coats 
   TABLE DATA           G   COPY public.coats (coat_id, product_id, size, description) FROM stdin;
    public          postgres    false    225   �       `          0    16582    hats 
   TABLE DATA           ?   COPY public.hats (hat_id, product_id, description) FROM stdin;
    public          postgres    false    223   )�       f          0    16627    hoodies 
   TABLE DATA           V   COPY public.hoodies (hoodie_id, product_id, size, with_hood, description) FROM stdin;
    public          postgres    false    229   F�       P          0    16452    orders 
   TABLE DATA           s   COPY public.orders (order_id, product_id, user_id, order_date, payment_method, order_status, quantity) FROM stdin;
    public          postgres    false    207   c�       R          0    16473    pants 
   TABLE DATA           G   COPY public.pants (pant_id, product_id, size, description) FROM stdin;
    public          postgres    false    209   ��       N          0    16431    products 
   TABLE DATA           �   COPY public.products (product_id, name, color, quantity, user_id, category_id, gender, brand, material, date, picture, price) FROM stdin;
    public          postgres    false    205   ��       Z          0    16537    scarves 
   TABLE DATA           D   COPY public.scarves (scarf_id, product_id, description) FROM stdin;
    public          postgres    false    217   ��       T          0    16489    shoes 
   TABLE DATA           G   COPY public.shoes (shoe_id, product_id, size, description) FROM stdin;
    public          postgres    false    211   א       X          0    16521    skirts 
   TABLE DATA           I   COPY public.skirts (skirt_id, product_id, size, description) FROM stdin;
    public          postgres    false    215   ��       \          0    16553    socks 
   TABLE DATA           A   COPY public.socks (sock_id, product_id, description) FROM stdin;
    public          postgres    false    219   �       d          0    16611    tshirts 
   TABLE DATA           K   COPY public.tshirts (tshirt_id, product_id, size, description) FROM stdin;
    public          postgres    false    227   .�       L          0    16420    users 
   TABLE DATA           �   COPY public.users (user_id, postal_code, address, first_name, last_name, national_code, phone_number, birth_date, user_type, password) FROM stdin;
    public          postgres    false    203   K�       |           0    0    bags_bag_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.bags_bag_id_seq', 1, false);
          public          postgres    false    220            }           0    0    belts_belt_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.belts_belt_id_seq', 1, false);
          public          postgres    false    212            ~           0    0    categories_category_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.categories_category_id_seq', 1, false);
          public          postgres    false    200                       0    0    coats_coat_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.coats_coat_id_seq', 1, false);
          public          postgres    false    224            �           0    0    hats_hat_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.hats_hat_id_seq', 1, false);
          public          postgres    false    222            �           0    0    hoodies_hoodie_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.hoodies_hoodie_id_seq', 1, false);
          public          postgres    false    228            �           0    0    orders_order_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.orders_order_id_seq', 1, false);
          public          postgres    false    206            �           0    0    pants_pant_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.pants_pant_id_seq', 1, false);
          public          postgres    false    208            �           0    0    products_product_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.products_product_id_seq', 1, false);
          public          postgres    false    204            �           0    0    scarves_scarf_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.scarves_scarf_id_seq', 1, false);
          public          postgres    false    216            �           0    0    shoes_shoe_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.shoes_shoe_id_seq', 1, false);
          public          postgres    false    210            �           0    0    skirts_skirt_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.skirts_skirt_id_seq', 1, false);
          public          postgres    false    214            �           0    0    socks_sock_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.socks_sock_id_seq', 1, false);
          public          postgres    false    218            �           0    0    tshirts_tshirt_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.tshirts_tshirt_id_seq', 1, false);
          public          postgres    false    226            �           0    0    users_user_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.users_user_id_seq', 29, true);
          public          postgres    false    202            �           2606    16574    bags bags_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.bags
    ADD CONSTRAINT bags_pkey PRIMARY KEY (bag_id);
 8   ALTER TABLE ONLY public.bags DROP CONSTRAINT bags_pkey;
       public            postgres    false    221            �           2606    16513    belts belts_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.belts
    ADD CONSTRAINT belts_pkey PRIMARY KEY (belt_id);
 :   ALTER TABLE ONLY public.belts DROP CONSTRAINT belts_pkey;
       public            postgres    false    213            �           2606    16417    categories categories_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category_id);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public            postgres    false    201            �           2606    16603    coats coats_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.coats
    ADD CONSTRAINT coats_pkey PRIMARY KEY (coat_id);
 :   ALTER TABLE ONLY public.coats DROP CONSTRAINT coats_pkey;
       public            postgres    false    225            �           2606    16587    hats hats_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.hats
    ADD CONSTRAINT hats_pkey PRIMARY KEY (hat_id);
 8   ALTER TABLE ONLY public.hats DROP CONSTRAINT hats_pkey;
       public            postgres    false    223            �           2606    16635    hoodies hoodies_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.hoodies
    ADD CONSTRAINT hoodies_pkey PRIMARY KEY (hoodie_id);
 >   ALTER TABLE ONLY public.hoodies DROP CONSTRAINT hoodies_pkey;
       public            postgres    false    229            �           2606    16460    orders orders_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);
 <   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_pkey;
       public            postgres    false    207            �           2606    16481    pants pants_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.pants
    ADD CONSTRAINT pants_pkey PRIMARY KEY (pant_id);
 :   ALTER TABLE ONLY public.pants DROP CONSTRAINT pants_pkey;
       public            postgres    false    209            �           2606    16439    products products_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);
 @   ALTER TABLE ONLY public.products DROP CONSTRAINT products_pkey;
       public            postgres    false    205            �           2606    16545    scarves scarves_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.scarves
    ADD CONSTRAINT scarves_pkey PRIMARY KEY (scarf_id);
 >   ALTER TABLE ONLY public.scarves DROP CONSTRAINT scarves_pkey;
       public            postgres    false    217            �           2606    16497    shoes shoes_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.shoes
    ADD CONSTRAINT shoes_pkey PRIMARY KEY (shoe_id);
 :   ALTER TABLE ONLY public.shoes DROP CONSTRAINT shoes_pkey;
       public            postgres    false    211            �           2606    16529    skirts skirts_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.skirts
    ADD CONSTRAINT skirts_pkey PRIMARY KEY (skirt_id);
 <   ALTER TABLE ONLY public.skirts DROP CONSTRAINT skirts_pkey;
       public            postgres    false    215            �           2606    16561    socks socks_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.socks
    ADD CONSTRAINT socks_pkey PRIMARY KEY (sock_id);
 :   ALTER TABLE ONLY public.socks DROP CONSTRAINT socks_pkey;
       public            postgres    false    219            �           2606    16619    tshirts tshirts_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.tshirts
    ADD CONSTRAINT tshirts_pkey PRIMARY KEY (tshirt_id);
 >   ALTER TABLE ONLY public.tshirts DROP CONSTRAINT tshirts_pkey;
       public            postgres    false    227            �           2606    16428    users users_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    203            �           1259    16643    idx_productid    INDEX     H   CREATE INDEX idx_productid ON public.products USING btree (product_id);
 !   DROP INDEX public.idx_productid;
       public            postgres    false    205            �           1259    16644 )   idx_users_firstname_lastname_nationalcode    INDEX     {   CREATE INDEX idx_users_firstname_lastname_nationalcode ON public.users USING btree (first_name, last_name, national_code);
 =   DROP INDEX public.idx_users_firstname_lastname_nationalcode;
       public            postgres    false    203    203    203            �           1259    16645    idx_users_postalcode    INDEX     M   CREATE INDEX idx_users_postalcode ON public.users USING btree (postal_code);
 (   DROP INDEX public.idx_users_postalcode;
       public            postgres    false    203            �           2606    16575    bags bags_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.bags
    ADD CONSTRAINT bags_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 C   ALTER TABLE ONLY public.bags DROP CONSTRAINT bags_product_id_fkey;
       public          postgres    false    221    205    2975            �           2606    16514    belts belts_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.belts
    ADD CONSTRAINT belts_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 E   ALTER TABLE ONLY public.belts DROP CONSTRAINT belts_product_id_fkey;
       public          postgres    false    213    205    2975            �           2606    16604    coats coats_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.coats
    ADD CONSTRAINT coats_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 E   ALTER TABLE ONLY public.coats DROP CONSTRAINT coats_product_id_fkey;
       public          postgres    false    2975    205    225            �           2606    16588    hats hats_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.hats
    ADD CONSTRAINT hats_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 C   ALTER TABLE ONLY public.hats DROP CONSTRAINT hats_product_id_fkey;
       public          postgres    false    205    2975    223            �           2606    16636    hoodies hoodies_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.hoodies
    ADD CONSTRAINT hoodies_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 I   ALTER TABLE ONLY public.hoodies DROP CONSTRAINT hoodies_product_id_fkey;
       public          postgres    false    229    205    2975            �           2606    16461    orders orders_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 G   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_product_id_fkey;
       public          postgres    false    207    2975    205            �           2606    16466    orders orders_user_id_fkey    FK CONSTRAINT     ~   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);
 D   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_user_id_fkey;
       public          postgres    false    203    207    2972            �           2606    16482    pants pants_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.pants
    ADD CONSTRAINT pants_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 E   ALTER TABLE ONLY public.pants DROP CONSTRAINT pants_product_id_fkey;
       public          postgres    false    2975    205    209            �           2606    16445 "   products products_category_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(category_id);
 L   ALTER TABLE ONLY public.products DROP CONSTRAINT products_category_id_fkey;
       public          postgres    false    201    205    2968            �           2606    16440    products products_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);
 H   ALTER TABLE ONLY public.products DROP CONSTRAINT products_user_id_fkey;
       public          postgres    false    2972    205    203            �           2606    16546    scarves scarves_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.scarves
    ADD CONSTRAINT scarves_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 I   ALTER TABLE ONLY public.scarves DROP CONSTRAINT scarves_product_id_fkey;
       public          postgres    false    2975    205    217            �           2606    16498    shoes shoes_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.shoes
    ADD CONSTRAINT shoes_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 E   ALTER TABLE ONLY public.shoes DROP CONSTRAINT shoes_product_id_fkey;
       public          postgres    false    205    211    2975            �           2606    16530    skirts skirts_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.skirts
    ADD CONSTRAINT skirts_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 G   ALTER TABLE ONLY public.skirts DROP CONSTRAINT skirts_product_id_fkey;
       public          postgres    false    205    2975    215            �           2606    16562    socks socks_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.socks
    ADD CONSTRAINT socks_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 E   ALTER TABLE ONLY public.socks DROP CONSTRAINT socks_product_id_fkey;
       public          postgres    false    205    219    2975            �           2606    16620    tshirts tshirts_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tshirts
    ADD CONSTRAINT tshirts_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 I   ALTER TABLE ONLY public.tshirts DROP CONSTRAINT tshirts_product_id_fkey;
       public          postgres    false    205    2975    227            ^      x������ � �      V      x������ � �      J      x������ � �      b      x������ � �      `      x������ � �      f      x������ � �      P      x������ � �      R      x������ � �      N      x������ � �      Z      x������ � �      T      x������ � �      X      x������ � �      \      x������ � �      d      x������ � �      L      x������ � �     
import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('Music.sqlite')
cur = conn.cursor()

#建表
cur.executescript('''
    DROP TABLE IF EXIST Artist;
    DROP TABLE IF EXIST Genre;
    DROP TABLE IF EXIST Album;
    DROP TABLE IF EXIST Track;

    CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
    );

    CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
    );

    CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
    );
    ''')

#解译XML文件至各个dict节点
fname = input('Please enter the file name')
if fname < 1: fname = 'Library.xml'
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')



#寻找匹配的函数
def scan(d, key):
    found = False
    for inf in d:
        tag = inf.find('key')
        if tag: return tag.text
    
    return found








for event in all:
    if scan












    

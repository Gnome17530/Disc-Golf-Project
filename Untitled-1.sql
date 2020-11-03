-- SQLite
select disc.imgurl, disc.description, category.description from disc
join category on category.id=disc.category_id;
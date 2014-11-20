/* PICKS OUT HASH TAGS FOR CATEGORIES */

/* REQUIREMENTS: Python, BeautifulSoup */

/*EXCLUDE LIST*/ exclude.txt  /*if there is a space use '+'*/
/* THIS TEXT FILE CONTAINS LIST OF TAGS YOU DONT WANT TO DOWNLOAD> THIS IS IN CASE YOU HAVE LAREADY DOWNLOADED THE
 * CONTENT AND IT STOPPED FOR SOME REASON MID WAY*/


/*FORMATTING*/
INPUT: Name of the file which contains list of categories for which the tags are needed.
OUTPUT: DIR_categoryname for each category. Each such directory will have subdirectories dedicated to a particular tag.
The tag directories will have GIFS_DIR and TAG_DIR containing gifs and corresponding tags respectively.

/*MAIN FILE*/
testScript.py  --argv[1] categoryFile.txt


/*CLASS DETAILS*/

CLASS : CatchCatPage /*Catches the category page and retrieves the tags present in it*/
CLASS : CatchTagGIFs /*Corresponding to each TAG retrieve at max 100 results for each tag and save them in the proper format*/


שם הפרוייקט**: library-api **

כמה מילים על הפרוייקט : הפרוייקט מדמה לנו מערכת לניהול בתוך ספרייה  את כל הניהול שצריך בתוך ספריה לחיקה החזרה של ספרים ת יצירת ספר חדש תמנהל מערך של מנויים עם כל האפשרויות של הוספה הסרה וכו, שעובת על בסיס נתונים ב(database )

**להריץ את הדוקר וליצור אתה הדאטה בייס** 

docker run --name library_db \-e MYSQL_ROOT_PASSWORD=secret \-e MYSQL_DATABASE=mydb \-p 3306:3306 \-d mysql:latest


docker exec -it  library_db mysql -u root -p קוד לכניסה לקונטטינר

מבנה התקיות:**
ibrary-api/  תקיה ראשית :
│  
├── app/  
│   ├── main.py  מנהל את כל השרת  
│   ├── database/  תקיה של ניהול מול הזיכרון 
│   │   ├── db\_connection.py  תקיה שבה אני מקשר בין פיתון לבין הדאטה ביס
│   │   ├── book\_db.py  ניהול של הספרים מול הדאטה בייס 
│   │   └── member\_db.py   ניהול של המשתשמים בספריה מול הדאטה בייס 
│   ├── routes/  ניהול של של השרת ראוטר לנהל עפ הבקשה באינרטנט לר=
│   │   ├── book\_routes.py  לקבל מידע עפ בקשה לעניין של הספרים 
│   │   ├── member\_routes.py   לקבל מידע עפ בקשה של משתשמים 
│   │   └── report\_routes.py  דיווח 
│   └── logs/  
│       └── app.log  קובץ לןדג שבו מביאים את הערות על התוכנית 
│  
├── README.md  
├── requirements.txt  קובץ שנמצא עם כל הדברים שצריך להתקין 
└── .gitignore


בפרוייקט אנחנו מנהלים את הזיכרון על ידי שלוש טבאות שנמצאות בזיכרון שלנו 
טבלה ראשונה book : 
יש לנו id : שמקבל רק מספר מתאים שאחד לא דומה לשני ( INT AUTO_INCREMENT PRIMARY KEY)

title : כותרת הספר, עמודה לא ריקה, מקסימום 50 תווים(VARCHAR(50) NOT NULL )

outhor : שם המחבר, עמודה לא ריקה, מקסימום 50 תווים(VARCHAR(50) NOT NULL )

genre : ערכי `genre` מותרים:**  Fiction | Non-Fiction | Science | History | Other — מומש כעמודת ENUM במסד הנתונים, כל ערך אחר מחזיר שגיאה, עמודה לא ריקה  (NOT NULL)

is_available: האם הסmembersפר זמין להשאלה — FALSE מסמן הושאל עמודה לא ריקה 

borrowed_by_member_id:  מזהה החבר שמחזיק את הספר — NULL אם זמין

טבלה שניה בזיכרון members:

id : שמקבל רק מספר מתאים שאחד לא דומה לשני( INT AUTO_INCREMENT PRIMARY KEY)

name:שם החבר, עמודה לא ריקה, מקסימום 50 תווים (VARCHAR(50) NOT NULL )

email : תובת מייל — ייחודית, עמודה לא ריקה(NOT NUL)

is_active:  האם החבר פעיל — FALSE לא יכול להשאיל עמודה לא ריקה  ( NOT NULL )

total_borrows : מונה סה"כ השאלות — עולה ב-1 בכל השאלה עמודה לא ריקה( NOT NULL )

אחרי שאנחנו כותבים את הטבלאות בזיכרון ומגדירים מה כל  שדה בקבל ואיזה הגבלות יש לו אנחנו כותבים את הקוד בשיטת oop:

אז קודם יש לנו שני פונקציות שנמצאות בתוך תקיה של 
db_connection.py 
ובפנים יש 
get_connection :  יוצר חיבור ל-MySQL — כל מחלקת DB משתמשת בה

create_tables : יוצר את טבלאות books ו-members אם לא קיימות — רץ בעליית השרת, בתחילת פונק main |

בoop  יש שני מחלקחות 

 הן עובדות מול הדאטה בייס על פי בקשה

מחלקה ראשונה BookDB:

create_book :  יוצר ספר חדש 

get_all_books : מחזיר את כל הספרים 

get_book_by_id : מחזיר את הספר על ידי ה id 

update_book : מעדכן שדות בספר 

set_available : בןדק אם הספר זמין ואם כן מעדכן

count_total_books : סופר את סך כל הספרים במסד הנתונים

count_available_books : הספרים הזמינים  סופר את 

count_borrowed_books :  סופר את כמות הספרים הלא זמינים 

count_by_genre : סופר ספרים על ידי זאנר מסויים

count_active_borrows_by_member : סופר את כמה ספרים החבר מחזיק כרגע 

מחלקה שניה MemberDB:

get_all_members : פונקציה שמחזירה את כל רשימת החברים 

get_member_by_id : מחזיר חבר אחד על ידי הid  של כל אחד 

update_member : מעדכן שדות בטבלת הזיכרון 

deactivate_member : לבטל חבר שנמצא בספרייה 

activate_member : להפעיל חבר 

increment_borrows:מעלה את ההלוואה של הספר ב1 

count_active_members: סןפר כמה חברים יש לי פעילים 

get_top_member : מחזיר את החבר שלקח הכי הרבה ספרים



**טיפול בלוגים**

הודעה של פעולה הולכת לקובץ לוג והיא נמצאת 
עם הודעה של זמן ,רמה ,והודעה של מה קרה בתוכנית 

**טיפול בנקודות קצה של הלקוח שמבקש מהשרת**

Books :

POST : /books  : יצירת הספר 

GET  : /books : מביא את כל הספרים 

GET : //books/{id}  : מביא ספר ע"י id 

PATCH  : /books/{id} : מעדכן את הספר ע"י id

PATCH  : /books/{id}/borrow/{member_id} :השאלה של ספר לחבר 

PATCH : /books/{id}/return/{member_id} : החזרת ספר מחבר ששאל את הספר 

Members:

POST : /members : יצירת חבר חדש 

GET  : /members : מחזירה את כלל החברים 

GET  : members/{id} : מחזירה את החבר על ידי   id

PATCH  :  /members/{id}  : מעדכן חבר על ידי id 

PATCH  : /members/{id}/deactivate : עדכון של השבתה של חבר פעיל 

PATCH   : /members/{id}/activate  :  הפעלת חבר 


Reports :


GET : /reports/summary : מביא דוח כללי
GET : /reports/books-by-genre : מביא ספר לי הזאנר 
GET : /reports/top-member : מביא את החבר הכי פעיל 


**הרצה של הקובץ uvicorn main:app --reload***




{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "39166dfe",
   "metadata": {},
   "source": [
    "# SQL-проект Исследование данных об инвестиции венчурных фондов в компании-стартапы"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e7fae9ed",
   "metadata": {},
   "source": [
    "**Данные**   \n",
    "В проекте работа идёт с базой данных, которая хранит информацию о венчурных фондах и инвестициях в компании-стартапы. Эта база данных основана на датасете Startup Investments, опубликованном на популярной платформе для соревнований по исследованию данных Kaggle.  "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ef3d0a7",
   "metadata": {},
   "source": [
    "**Задача**   \n",
    "Проанализировать данные о фондах и инвестициях, произвести выгрузки данных и ответить на поставленные вопросы с помощью SQL."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb81312a",
   "metadata": {},
   "source": [
    "## Задания:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96e82759",
   "metadata": {},
   "source": [
    "### Задание 1\n",
    "Посчитайте, сколько компаний закрылось."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0476c479",
   "metadata": {},
   "source": [
    "'''   \n",
    "SELECT COUNT(name)   \n",
    "FROM company   \n",
    "WHERE status ='closed'    \n",
    ";   \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3e80389d",
   "metadata": {},
   "source": [
    "### Задание 2\n",
    "Отобразите количество привлечённых средств для новостных компаний США.  \n",
    "Используйте данные из таблицы company. Отсортируйте таблицу по убыванию значений в поле funding_total."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e9a2c4a",
   "metadata": {},
   "source": [
    "'''   \n",
    "SELECT funding_total   \n",
    "FROM company  \n",
    "WHERE category_code ='news' AND country_code='USA'   \n",
    "ORDER BY funding_total DESC;  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7da6f1cf",
   "metadata": {},
   "source": [
    "### Задание 3\n",
    "Найдите общую сумму сделок по покупке одних компаний другими в долларах. Отберите сделки, которые осуществлялись только за наличные с 2011 по 2013 год включительно."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa447cb5",
   "metadata": {},
   "source": [
    "'''   \n",
    "SELECT SUM(price_amount)  \n",
    "FROM acquisition  \n",
    "WHERE term_code = 'cash'  \n",
    "    AND EXTRACT(YEAR FROM CAST(acquired_at AS timestamp)) BETWEEN 2011 AND 2013;    \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8032ee70",
   "metadata": {},
   "source": [
    "### Задание 4\n",
    "Отобразите имя, фамилию и названия аккаунтов людей в твиттере, у которых названия аккаунтов начинаются на 'Silver'."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03db9b15",
   "metadata": {},
   "source": [
    "'''   \n",
    "SELECT first_name,  \n",
    "       last_name,  \n",
    "       twitter_username  \n",
    "FROM people  \n",
    "WHERE twitter_username LIKE 'Silver%';  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ef400518",
   "metadata": {},
   "source": [
    "### Задание 5\n",
    "Вывести на экран всю информацию о людях, у которых названия аккаунтов в твиттере содержат подстроку 'money', а фамилия начинается на 'K'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1f305d1a",
   "metadata": {},
   "source": [
    "'''   \n",
    "SELECT *  \n",
    "FROM people  \n",
    "WHERE twitter_username LIKE '%money%'   \n",
    "     AND last_name LIKE 'K%';  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d03ed147",
   "metadata": {},
   "source": [
    "### Задание 6\n",
    "Для каждой страны отобразите общую сумму привлечённых инвестиций, которые получили компании, зарегистрированные в этой стране. Страну, в которой зарегистрирована компания, можно определить по коду страны. Отсортируйте данные по убыванию суммы."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "88923fe2",
   "metadata": {},
   "source": [
    "'''   \n",
    "SELECT country_code,  \n",
    "       SUM(funding_total)  \n",
    "FROM company  \n",
    "GROUP BY country_code  \n",
    "ORDER BY SUM(funding_total) DESC;  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cd8aea3e",
   "metadata": {},
   "source": [
    "### Задание 7\n",
    "Составьте таблицу, в которую войдёт дата проведения раунда, а также минимальное и максимальное значения суммы инвестиций, привлечённых в эту дату.\n",
    "Оставьте в итоговой таблице только те записи, в которых минимальное значение суммы инвестиций не равно нулю и не равно максимальному значению."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2e3099c",
   "metadata": {},
   "source": [
    "'''  \n",
    "SELECT CAST(funded_at AS date),  \n",
    "       MIN(raised_amount),  \n",
    "       MAX(raised_amount)  \n",
    "FROM funding_round  \n",
    "GROUP BY CAST(funded_at AS date)  \n",
    "HAVING  MIN(raised_amount) != 0  \n",
    "      AND MIN(raised_amount) != MAX(raised_amount);  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ff40fd3b",
   "metadata": {},
   "source": [
    "### Задание 8\n",
    "\n",
    "Создайте поле с категориями:   \n",
    "- Для фондов, которые инвестируют в 100 и более компаний, назначьте категорию high_activity.   \n",
    "- Для фондов, которые инвестируют в 20 и более компаний до 100, назначьте категорию middle_activity.  \n",
    "- Если количество инвестируемых компаний фонда не достигает 20, назначьте категорию low_activity.  \n",
    "\n",
    "Отобразите все поля таблицы fund и новое поле с категориями."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c786e665",
   "metadata": {},
   "source": [
    "'''  \n",
    "SELECT *,  \n",
    "          CASE  \n",
    "           WHEN invested_companies  >= 100 THEN 'high_activity'  \n",
    "           WHEN invested_companies >= 20 AND invested_companies < 100 THEN 'middle_activity'  \n",
    "           WHEN invested_companies <= 20 THEN 'low_activity'  \n",
    "       END       \n",
    "FROM fund;  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b892c1a",
   "metadata": {},
   "source": [
    "### Задание 9\n",
    "Для каждой из категорий, назначенных в предыдущем задании, посчитайте округлённое до ближайшего целого числа среднее количество инвестиционных раундов, в которых фонд принимал участие. Выведите на экран категории и среднее число инвестиционных раундов. Отсортируйте таблицу по возрастанию среднего."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0078cda1",
   "metadata": {},
   "source": [
    "'''  \n",
    "SELECT CASE  \n",
    "           WHEN invested_companies>=100 THEN 'high_activity'  \n",
    "           WHEN invested_companies>=20 THEN 'middle_activity'  \n",
    "           ELSE 'low_activity'  \n",
    "       END AS activity,  \n",
    "       ROUND(AVG(investment_rounds))  \n",
    "FROM fund  \n",
    "GROUP BY activity  \n",
    "ORDER BY ROUND(AVG(investment_rounds));  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aec65d66",
   "metadata": {},
   "source": [
    "### Задание 10\n",
    "Выгрузите таблицу с десятью самыми активными инвестирующими странами. Активность страны определите по среднему количеству компаний, в которые инвестируют фонды этой страны.  \n",
    "Для каждой страны посчитайте минимальное, максимальное и среднее число компаний, в которые инвестировали фонды, основанные с 2010 по 2012 год включительно.  \n",
    "Исключите из таблицы страны с фондами, у которых минимальное число компаний, получивших инвестиции, равно нулю.   Отсортируйте таблицу по среднему количеству компаний от большего к меньшему.  \n",
    "Для фильтрации диапазона по годам используйте оператор BETWEEN."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bcb30b4e",
   "metadata": {},
   "source": [
    "'''  \n",
    "SELECT country_code,  \n",
    "       AVG(invested_companies),  \n",
    "       MIN(invested_companies),  \n",
    "       MAX(invested_companies)  \n",
    "FROM fund  \n",
    "WHERE EXTRACT(YEAR FROM CAST(founded_at AS date)) BETWEEN '2010' AND '2012'  \n",
    "GROUP BY country_code  \n",
    "HAVING MIN(invested_companies) != 0  \n",
    "ORDER BY AVG(invested_companies) DESC  \n",
    "LIMIT 10;  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5df88109",
   "metadata": {},
   "source": [
    "### Задание 11\n",
    "Отобразите имя и фамилию всех сотрудников стартапов. Добавьте поле с названием учебного заведения, которое окончил сотрудник, если эта информация известна."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2b935829",
   "metadata": {},
   "source": [
    "'''  \n",
    "SELECT p.first_name,  \n",
    "       p.last_name,  \n",
    "       e.instituition  \n",
    "FROM people AS p  \n",
    "LEFT JOIN education AS e ON e.person_id=p.id;  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b0956689",
   "metadata": {},
   "source": [
    "### Задание 12\n",
    "Для каждой компании найдите количество учебных заведений, которые окончили её сотрудники. Выведите название компании и число уникальных названий учебных заведений. Составьте топ-5 компаний по количеству университетов."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3174c0d4",
   "metadata": {},
   "source": [
    "'''  \n",
    "SELECT  c.name,  \n",
    "      COUNT(DISTINCT e.instituition)  \n",
    "FROM company AS c        \n",
    "JOIN people AS p ON c.id=p.company_id  \n",
    "JOIN education AS e ON p.id=e.person_id  \n",
    "GROUP BY c.name  \n",
    "ORDER BY COUNT(DISTINCT e.instituition) DESC  \n",
    "LIMIT 5;  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3b0335e",
   "metadata": {},
   "source": [
    "### Задание 13\n",
    "Составьте список с уникальными названиями закрытых компаний, для которых первый раунд финансирования оказался последним."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "24d72776",
   "metadata": {},
   "source": [
    "'''  \n",
    "SELECT DISTINCT name  \n",
    "                     FROM company   \n",
    "                     WHERE id IN (SELECT company_id  \n",
    "                                  FROM funding_round  \n",
    "                                  WHERE is_first_round = 1 AND is_last_round = 1)  \n",
    "                     AND status = 'closed';  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "943ae4b1",
   "metadata": {},
   "source": [
    "### Задание 14\n",
    "Составьте список уникальных номеров сотрудников, которые работают в компаниях, отобранных в предыдущем задании."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a896d449",
   "metadata": {},
   "source": [
    "'''  \n",
    "SELECT DISTINCT p.id               \n",
    "FROM people AS p  \n",
    "WHERE company_id IN (SELECT id  \n",
    "                     FROM company   \n",
    "                     WHERE id IN (SELECT company_id  \n",
    "                                  FROM funding_round  \n",
    "                                  WHERE is_first_round = 1 AND is_last_round = 1)   \n",
    "                     AND status = 'closed');  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e786acc",
   "metadata": {},
   "source": [
    "### Задание 15\n",
    "Составьте таблицу, куда войдут уникальные пары с номерами сотрудников из предыдущей задачи и учебным заведением, которое окончил сотрудник."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1cb05dfb",
   "metadata": {},
   "source": [
    "'''  \n",
    "SELECT DISTINCT p.id,  \n",
    "                e.instituition  \n",
    "FROM people AS p JOIN education AS e ON p.id = e.person_id  \n",
    "WHERE company_id IN (SELECT id  \n",
    "                     FROM company  \n",
    "                     WHERE id IN (SELECT company_id  \n",
    "                                  FROM funding_round  \n",
    "                                  WHERE is_first_round = 1 AND is_last_round = 1)  \n",
    "                     AND status = 'closed');  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c093b666",
   "metadata": {},
   "source": [
    "### Задание 16\n",
    "Посчитайте количество учебных заведений для каждого сотрудника из предыдущего задания."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20bf4549",
   "metadata": {},
   "source": [
    "'''  \n",
    "SELECT DISTINCT p.id,  \n",
    "                COUNT(e.instituition)  \n",
    "FROM people AS p JOIN education AS e ON p.id = e.person_id  \n",
    "WHERE company_id IN (SELECT id  \n",
    "                     FROM company   \n",
    "                     WHERE id IN (SELECT company_id  \n",
    "                                  FROM funding_round  \n",
    "                                  WHERE is_first_round = 1 AND is_last_round = 1)  \n",
    "                     AND status = 'closed')  \n",
    "GROUP BY p.id;  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c9a94630",
   "metadata": {},
   "source": [
    "### Задание 17\n",
    "Дополните предыдущий запрос и выведите среднее число учебных заведений, которые окончили сотрудники разных компаний. Нужно вывести только одну запись, группировка здесь не понадобится."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47ee1754",
   "metadata": {},
   "source": [
    "'''  \n",
    "WITH  \n",
    "res AS (SELECT p.id,   \n",
    "      COUNT(e.instituition) AS total_instituition  \n",
    "      FROM people AS p JOIN education AS e ON p.id = e.person_id  \n",
    "      WHERE company_id IN (SELECT id  \n",
    "                     FROM company   \n",
    "                     WHERE id IN (SELECT company_id  \n",
    "                                  FROM funding_round  \n",
    "                                  WHERE is_first_round = 1 AND is_last_round = 1)  \n",
    "                     AND status = 'closed')  \n",
    "       GROUP BY p.id)  \n",
    "  \n",
    "SELECT AVG(res.total_instituition)  \n",
    "FROM res;  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "06055b08",
   "metadata": {},
   "source": [
    "### Задание 18\n",
    "\n",
    "Напишите похожий запрос: выведите среднее число учебных заведений, которые окончили сотрудники компании Facebook."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17874ec1",
   "metadata": {},
   "source": [
    "'''  \n",
    "WITH  \n",
    "res AS (SELECT p.id,   \n",
    "      COUNT(e.instituition) AS total_instituition  \n",
    "      FROM people AS p JOIN education AS e ON p.id = e.person_id  \n",
    "      WHERE company_id IN (SELECT id  \n",
    "                     FROM company   \n",
    "                     WHERE name = 'Facebook')  \n",
    "       GROUP BY p.id)  \n",
    "  \n",
    "SELECT AVG(res.total_instituition)  \n",
    "FROM res;  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d6143a5",
   "metadata": {},
   "source": [
    "### Задание 19\n",
    "Составьте таблицу из полей:  \n",
    "- name_of_fund — название фонда;  \n",
    "- name_of_company — название компании;  \n",
    "- amount — сумма инвестиций, которую привлекла компания в раунде.  \n",
    "\n",
    "В таблицу войдут данные о компаниях, в истории которых было больше шести важных этапов, а раунды финансирования проходили с 2012 по 2013 год включительно."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7d48811d",
   "metadata": {},
   "source": [
    "'''  \n",
    "WITH funding_round_filer AS  \n",
    "(SELECT *  \n",
    "FROM funding_round  \n",
    "WHERE EXTRACT(YEAR FROM CAST(funded_at AS date)) IN (2012, 2013))  \n",
    "  \n",
    "SELECT  \n",
    "f.name AS name_of_fund,  \n",
    "c.name AS name_of_company,  \n",
    "fr.raised_amount AS amount  \n",
    "  \n",
    "FROM investment AS i LEFT JOIN company AS c ON c.id = i.company_id  \n",
    "LEFT JOIN fund AS f ON f.id=i.fund_id  \n",
    "  \n",
    "JOIN funding_round_filer AS fr ON fr.id = i.funding_round_id  \n",
    "WHERE c.milestones > 6;  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81f931f5",
   "metadata": {},
   "source": [
    "### Задание 20 \n",
    "Выгрузите таблицу, в которой будут такие поля:  \n",
    "- название компании-покупателя;  \n",
    "- сумма сделки;  \n",
    "- название компании, которую купили;  \n",
    "- сумма инвестиций, вложенных в купленную компанию;  \n",
    "- доля, которая отображает, во сколько раз сумма покупки превысила сумму вложенных в компанию инвестиций, округлённая до ближайшего целого числа.\n",
    "\n",
    "Не учитывайте те сделки, в которых сумма покупки равна нулю. Если сумма инвестиций в компанию равна нулю, исключите такую компанию из таблицы.  \n",
    "Отсортируйте таблицу по сумме сделки от большей к меньшей, а затем по названию купленной компании в алфавитном порядке. Ограничьте таблицу первыми десятью записями.  "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1a70d7e5",
   "metadata": {},
   "source": [
    "'''  \n",
    "SELECT c.name,  \n",
    "       a.price_amount,  \n",
    "       c_1.name,  \n",
    "\t   c_1.funding_total,  \n",
    "\t   ROUND(a.price_amount/c_1.funding_total) AS percent  \n",
    "FROM acquisition AS a  \n",
    "LEFT JOIN company AS c ON a.acquiring_company_id = c.id  \n",
    "LEFT JOIN company AS c_1 ON a.acquired_company_id = c_1.id  \n",
    "WHERE a.price_amount>0   \n",
    " AND c_1.funding_total>0  \n",
    "ORDER BY a.price_amount DESC  \n",
    "LIMIT 10;  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e3f65e7",
   "metadata": {},
   "source": [
    "### Задание 21\n",
    "Выгрузите таблицу, в которую войдут названия компаний из категории social, получившие финансирование с 2010 по 2013 год.   \n",
    "Выведите также номер месяца, в котором проходил раунд финансирования."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f03d4426",
   "metadata": {},
   "source": [
    "'''  \n",
    "SELECT c.name,  \n",
    "       EXTRACT(MONTH FROM CAST(funded_at AS date))  \n",
    "FROM company AS c  \n",
    "LEFT OUTER JOIN funding_round AS f ON c.id = f.company_id  \n",
    "WHERE EXTRACT(YEAR FROM CAST(funded_at AS date)) IN (2010, 2011, 2012, 2013)   \n",
    "      AND c.category_code = 'social';  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c7095bf8",
   "metadata": {},
   "source": [
    "### Задание 21  \n",
    "Отберите данные по месяцам с 2010 по 2013 год, когда проходили инвестиционные раунды.  \n",
    "Сгруппируйте данные по номеру месяца и получите таблицу, в которой будут поля:  \n",
    "- номер месяца, в котором проходили раунды;  \n",
    "- количество уникальных названий фондов из США, которые инвестировали в этом месяце;  \n",
    "- количество компаний, купленных за этот месяц;  \n",
    "- общая сумма сделок по покупкам в этом месяце."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8903b70d",
   "metadata": {},
   "source": [
    "'''  \n",
    "WITH   \n",
    "month_fund AS  \n",
    "     (SELECT EXTRACT(MONTH FROM CAST(funded_at AS date)) AS MONTH,  \n",
    "             COUNT(DISTINCT f.name) AS count_of_fund               \n",
    "      FROM funding_round AS fr  \n",
    "   LEFT JOIN investment AS i ON i.funding_round_id = fr.id  \n",
    "   LEFT JOIN fund AS f ON i.fund_id = f.id  \n",
    "   WHERE EXTRACT(YEAR FROM CAST(funded_at AS date)) BETWEEN 2010 AND 2013  \n",
    "   AND f.country_code='USA'  \n",
    "   GROUP BY MONTH),  \n",
    "        \n",
    "month_acquired AS  \n",
    "  (SELECT EXTRACT(MONTH FROM CAST(acquired_at  AS date)) AS MONTH,  \n",
    "          COUNT(acquiring_company_id) AS count_month_acquired,  \n",
    "          SUM(price_amount) AS sum_price_amount  \n",
    "   FROM acquisition  \n",
    "   WHERE EXTRACT(YEAR FROM CAST(acquired_at  AS date)) BETWEEN 2010 AND 2013  \n",
    "   GROUP BY MONTH)  \n",
    "    \n",
    "SELECT month_fund.MONTH,  \n",
    "       month_fund.count_of_fund,   \n",
    "       month_acquired.count_month_acquired,  \n",
    "       month_acquired.sum_price_amount  \n",
    "FROM month_fund  \n",
    "JOIN month_acquired ON month_fund.MONTH=month_acquired.MONTH;  \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cd7cc898",
   "metadata": {},
   "source": [
    "### Задание 21\n",
    "Составьте сводную таблицу и выведите среднюю сумму инвестиций для стран, в которых есть стартапы, зарегистрированные в 2011, 2012 и 2013 годах. Данные за каждый год должны быть в отдельном поле. Отсортируйте таблицу по среднему значению инвестиций за 2011 год от большего к меньшему."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "95d92cf7",
   "metadata": {},
   "source": [
    "'''   \n",
    "WITH   \n",
    "inv_2011 AS (SELECT country_code,  \n",
    "\t\t\t\t     AVG(funding_total) AS year_2011  \n",
    "\t\t     FROM company  \n",
    "\t\t     WHERE EXTRACT(YEAR FROM founded_at) = 2011  \n",
    "\t\t\t GROUP BY country_code),  \n",
    "inv_2012 AS (SELECT country_code,  \n",
    "\t\t\t\t    AVG(funding_total) AS year_2012  \n",
    "\t\t\t FROM company  \n",
    "\t\t\t WHERE EXTRACT(YEAR FROM founded_at) = 2012  \n",
    "\t\t\t GROUP BY country_code),  \n",
    "inv_2013 AS (SELECT country_code,   \n",
    "\t\t\t\t    AVG(funding_total) AS year_2013  \n",
    "\t\t\t FROM company  \n",
    "\t\t\t WHERE EXTRACT(YEAR FROM founded_at) = 2013  \n",
    "\t\t\t GROUP BY country_code)\t  \n",
    "  \n",
    "SELECT inv_2011.country_code,  \n",
    "       inv_2011.year_2011,  \n",
    "       inv_2012.year_2012,  \n",
    "       inv_2013.year_2013  \n",
    "FROM inv_2011  \n",
    "JOIN inv_2012 ON inv_2011.country_code=inv_2012.country_code  \n",
    "JOIN inv_2013 ON inv_2013.country_code=inv_2012.country_code  \n",
    "ORDER BY year_2011 DESC;   \n",
    "'''"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

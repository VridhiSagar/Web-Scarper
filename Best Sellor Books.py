{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "886e0a8d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<Response [200]>\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import random\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup\n",
    "import csv\n",
    "\n",
    "\n",
    "url = \"https://www.amazon.com/charts/mostsold/nonfiction/ref=bsm_char_sold_nonfict/ref=s9_acss_bw_cg_bsmmost_1a1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=71ZZE5ADT8J9PPR4GYR2&pf_rd_t=101&pf_rd_p=6be52979-aa91-4d19-9c0a-4b11ed3e5f6f&pf_rd_i=16857165011\" \n",
    "user_agents_list = [\n",
    "    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',\n",
    "    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',\n",
    "    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'\n",
    "]\n",
    "\n",
    "response = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})\n",
    "print(response)\n",
    "soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "# print(soup)\n",
    "jobs = []\n",
    "\n",
    "for job in soup.find_all(\"div\", {\"class\": \"kc-horizontal-rank-card desktop-hide mobile-hide row\"}):\n",
    "#     print(job)\n",
    "    title = job.find(\"div\", {\"class\": \"kc-rank-card-title\"}).text.strip()\n",
    "    author = job.find(\"div\", {\"class\": \"kc-rank-card-author\"}).text.strip()\n",
    "    pub = job.find(\"div\", {\"class\": \"kc-rank-card-publisher\"}).text.strip()\n",
    "#     description = job.find(\"div\", {\"class\": \"job_snippet\"}).text.strip()\n",
    "    \n",
    "    jobs.append({\"title\": title, \"author\": author, \"pub\": pub})\n",
    "\n",
    "for job in soup.find_all(\"div\", {\"class\": \"kc-horizontal-rank-card mobile-hide row\"}):\n",
    "#     print(job)\n",
    "    title = job.find(\"div\", {\"class\": \"kc-rank-card-title\"}).text.strip()\n",
    "    author = job.find(\"div\", {\"class\": \"kc-rank-card-author\"}).text.strip()\n",
    "    pub = job.find(\"div\", {\"class\": \"kc-rank-card-publisher\"}).text.strip()\n",
    "#     description = job.find(\"div\", {\"class\": \"job_snippet\"}).text.strip()\n",
    "    \n",
    "    jobs.append({\"title\": title, \"author\": author, \"pub\": pub})\n",
    "\n",
    "# print(jobs)\n",
    "jobs_df = pd.DataFrame(jobs)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "id": "55348624",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>author</th>\n",
       "      <th>pub</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>The Courage to Be Free</td>\n",
       "      <td>by Ron DeSantis</td>\n",
       "      <td>PUBLISHER: Broadside Books</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Atomic Habits</td>\n",
       "      <td>by James Clear</td>\n",
       "      <td>PUBLISHER: Avery</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Spare</td>\n",
       "      <td>by Prince Harry</td>\n",
       "      <td>PUBLISHER: Random House</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>The Subtle Art of Not Giving a F*ck</td>\n",
       "      <td>by Mark Manson</td>\n",
       "      <td>PUBLISHER: Harper</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Young Forever</td>\n",
       "      <td>by Dr. Mark Hyman, MD</td>\n",
       "      <td>PUBLISHER: Little, Brown Spark</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>The Body Keeps the Score</td>\n",
       "      <td>by Bessel van der Kolk, M.D.</td>\n",
       "      <td>PUBLISHER: Penguin Books</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>All My Knotted-Up Life</td>\n",
       "      <td>by Beth Moore</td>\n",
       "      <td>PUBLISHER: Tyndale House Publishers</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Never Split the Difference</td>\n",
       "      <td>by Chris Voss &amp; Tahl Raz</td>\n",
       "      <td>PUBLISHER: Harper Business</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>The 48 Laws of Power</td>\n",
       "      <td>by Robert Greene</td>\n",
       "      <td>PUBLISHER: Penguin Books</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Win Every Argument</td>\n",
       "      <td>by Mehdi Hasan</td>\n",
       "      <td>PUBLISHER: Henry Holt and Co.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>I'm Glad My Mom Died</td>\n",
       "      <td>by Jennette McCurdy</td>\n",
       "      <td>PUBLISHER: Simon &amp; Schuster</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Never Finished</td>\n",
       "      <td>by David Goggins</td>\n",
       "      <td>PUBLISHER: Lioncrest Publishing</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>8 Rules of Love</td>\n",
       "      <td>by Jay Shetty</td>\n",
       "      <td>PUBLISHER: Simon &amp; Schuster</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>The Creative Act</td>\n",
       "      <td>by Rick Rubin</td>\n",
       "      <td>PUBLISHER: Penguin Press</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Can't Hurt Me</td>\n",
       "      <td>by David Goggins</td>\n",
       "      <td>PUBLISHER: Lioncrest Publishing</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>12 Rules for Life</td>\n",
       "      <td>by Jordan B. Peterson</td>\n",
       "      <td>PUBLISHER: Random House Canada</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Rich Dad Poor Dad</td>\n",
       "      <td>by Robert T. Kiyosaki</td>\n",
       "      <td>PUBLISHER: Plata Publishing</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>The Four Agreements</td>\n",
       "      <td>by Don Miguel Ruiz &amp; Janet Mills</td>\n",
       "      <td>PUBLISHER: Amber-Allen Publishing</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Finding Me</td>\n",
       "      <td>by Viola Davis</td>\n",
       "      <td>PUBLISHER: HarperOne</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Baking Yesteryear</td>\n",
       "      <td>by B. Dylan Hollis</td>\n",
       "      <td>PUBLISHER: Alpha</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                  title                            author  \\\n",
       "0                The Courage to Be Free                   by Ron DeSantis   \n",
       "1                         Atomic Habits                    by James Clear   \n",
       "2                                 Spare                   by Prince Harry   \n",
       "3   The Subtle Art of Not Giving a F*ck                    by Mark Manson   \n",
       "4                         Young Forever             by Dr. Mark Hyman, MD   \n",
       "5              The Body Keeps the Score      by Bessel van der Kolk, M.D.   \n",
       "6                All My Knotted-Up Life                     by Beth Moore   \n",
       "7            Never Split the Difference          by Chris Voss & Tahl Raz   \n",
       "8                  The 48 Laws of Power                  by Robert Greene   \n",
       "9                    Win Every Argument                    by Mehdi Hasan   \n",
       "10                 I'm Glad My Mom Died               by Jennette McCurdy   \n",
       "11                       Never Finished                  by David Goggins   \n",
       "12                      8 Rules of Love                     by Jay Shetty   \n",
       "13                     The Creative Act                     by Rick Rubin   \n",
       "14                        Can't Hurt Me                  by David Goggins   \n",
       "15                    12 Rules for Life             by Jordan B. Peterson   \n",
       "16                    Rich Dad Poor Dad             by Robert T. Kiyosaki   \n",
       "17                  The Four Agreements  by Don Miguel Ruiz & Janet Mills   \n",
       "18                           Finding Me                    by Viola Davis   \n",
       "19                    Baking Yesteryear                by B. Dylan Hollis   \n",
       "\n",
       "                                    pub  \n",
       "0            PUBLISHER: Broadside Books  \n",
       "1                      PUBLISHER: Avery  \n",
       "2               PUBLISHER: Random House  \n",
       "3                     PUBLISHER: Harper  \n",
       "4        PUBLISHER: Little, Brown Spark  \n",
       "5              PUBLISHER: Penguin Books  \n",
       "6   PUBLISHER: Tyndale House Publishers  \n",
       "7            PUBLISHER: Harper Business  \n",
       "8              PUBLISHER: Penguin Books  \n",
       "9         PUBLISHER: Henry Holt and Co.  \n",
       "10          PUBLISHER: Simon & Schuster  \n",
       "11      PUBLISHER: Lioncrest Publishing  \n",
       "12          PUBLISHER: Simon & Schuster  \n",
       "13             PUBLISHER: Penguin Press  \n",
       "14      PUBLISHER: Lioncrest Publishing  \n",
       "15       PUBLISHER: Random House Canada  \n",
       "16          PUBLISHER: Plata Publishing  \n",
       "17    PUBLISHER: Amber-Allen Publishing  \n",
       "18                 PUBLISHER: HarperOne  \n",
       "19                     PUBLISHER: Alpha  "
      ]
     },
     "execution_count": 152,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jobs_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "cae29a2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "jobs_df[\"pub\"] = jobs_df[\"pub\"].str.slice(10)\n",
    "jobs_df[\"author\"] = jobs_df[\"author\"].str.slice(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "8a994280",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>author</th>\n",
       "      <th>pub</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>The Courage to Be Free</td>\n",
       "      <td>Ron DeSantis</td>\n",
       "      <td>Broadside Books</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Atomic Habits</td>\n",
       "      <td>James Clear</td>\n",
       "      <td>Avery</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Spare</td>\n",
       "      <td>Prince Harry</td>\n",
       "      <td>Random House</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>The Subtle Art of Not Giving a F*ck</td>\n",
       "      <td>Mark Manson</td>\n",
       "      <td>Harper</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Young Forever</td>\n",
       "      <td>Dr. Mark Hyman, MD</td>\n",
       "      <td>Little, Brown Spark</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>The Body Keeps the Score</td>\n",
       "      <td>Bessel van der Kolk, M.D.</td>\n",
       "      <td>Penguin Books</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>All My Knotted-Up Life</td>\n",
       "      <td>Beth Moore</td>\n",
       "      <td>Tyndale House Publishers</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Never Split the Difference</td>\n",
       "      <td>Chris Voss &amp; Tahl Raz</td>\n",
       "      <td>Harper Business</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>The 48 Laws of Power</td>\n",
       "      <td>Robert Greene</td>\n",
       "      <td>Penguin Books</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Win Every Argument</td>\n",
       "      <td>Mehdi Hasan</td>\n",
       "      <td>Henry Holt and Co.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>I'm Glad My Mom Died</td>\n",
       "      <td>Jennette McCurdy</td>\n",
       "      <td>Simon &amp; Schuster</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Never Finished</td>\n",
       "      <td>David Goggins</td>\n",
       "      <td>Lioncrest Publishing</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>8 Rules of Love</td>\n",
       "      <td>Jay Shetty</td>\n",
       "      <td>Simon &amp; Schuster</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>The Creative Act</td>\n",
       "      <td>Rick Rubin</td>\n",
       "      <td>Penguin Press</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Can't Hurt Me</td>\n",
       "      <td>David Goggins</td>\n",
       "      <td>Lioncrest Publishing</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>12 Rules for Life</td>\n",
       "      <td>Jordan B. Peterson</td>\n",
       "      <td>Random House Canada</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Rich Dad Poor Dad</td>\n",
       "      <td>Robert T. Kiyosaki</td>\n",
       "      <td>Plata Publishing</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>The Four Agreements</td>\n",
       "      <td>Don Miguel Ruiz &amp; Janet Mills</td>\n",
       "      <td>Amber-Allen Publishing</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Finding Me</td>\n",
       "      <td>Viola Davis</td>\n",
       "      <td>HarperOne</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Baking Yesteryear</td>\n",
       "      <td>B. Dylan Hollis</td>\n",
       "      <td>Alpha</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                  title                         author  \\\n",
       "0                The Courage to Be Free                   Ron DeSantis   \n",
       "1                         Atomic Habits                    James Clear   \n",
       "2                                 Spare                   Prince Harry   \n",
       "3   The Subtle Art of Not Giving a F*ck                    Mark Manson   \n",
       "4                         Young Forever             Dr. Mark Hyman, MD   \n",
       "5              The Body Keeps the Score      Bessel van der Kolk, M.D.   \n",
       "6                All My Knotted-Up Life                     Beth Moore   \n",
       "7            Never Split the Difference          Chris Voss & Tahl Raz   \n",
       "8                  The 48 Laws of Power                  Robert Greene   \n",
       "9                    Win Every Argument                    Mehdi Hasan   \n",
       "10                 I'm Glad My Mom Died               Jennette McCurdy   \n",
       "11                       Never Finished                  David Goggins   \n",
       "12                      8 Rules of Love                     Jay Shetty   \n",
       "13                     The Creative Act                     Rick Rubin   \n",
       "14                        Can't Hurt Me                  David Goggins   \n",
       "15                    12 Rules for Life             Jordan B. Peterson   \n",
       "16                    Rich Dad Poor Dad             Robert T. Kiyosaki   \n",
       "17                  The Four Agreements  Don Miguel Ruiz & Janet Mills   \n",
       "18                           Finding Me                    Viola Davis   \n",
       "19                    Baking Yesteryear                B. Dylan Hollis   \n",
       "\n",
       "                          pub  \n",
       "0             Broadside Books  \n",
       "1                       Avery  \n",
       "2                Random House  \n",
       "3                      Harper  \n",
       "4         Little, Brown Spark  \n",
       "5               Penguin Books  \n",
       "6    Tyndale House Publishers  \n",
       "7             Harper Business  \n",
       "8               Penguin Books  \n",
       "9          Henry Holt and Co.  \n",
       "10           Simon & Schuster  \n",
       "11       Lioncrest Publishing  \n",
       "12           Simon & Schuster  \n",
       "13              Penguin Press  \n",
       "14       Lioncrest Publishing  \n",
       "15        Random House Canada  \n",
       "16           Plata Publishing  \n",
       "17     Amber-Allen Publishing  \n",
       "18                  HarperOne  \n",
       "19                      Alpha  "
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jobs_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "id": "6d11e411",
   "metadata": {},
   "outputs": [],
   "source": [
    "jobs_df.to_csv(\"books_final.csv\", encoding='utf-8', index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "289cdea9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4dfd2fb4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9fbb0a69",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
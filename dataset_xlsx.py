{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "eb4c41c0-1454-45d4-975c-a421c4625bc4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                    Dates  Floats  Integers  Booleans\n",
      "index                                                \n",
      "0     2020-01-01 10:13:00  2222.0         1      True\n",
      "1     2020-01-02 00:00:00     NaN         2     False\n",
      "2     2020-01-02 00:00:00     inf         3      True\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import datetime as dt\n",
    "\n",
    "# Crie uma lista de dados\n",
    "\n",
    "data = [\n",
    "    [dt.datetime(2020, 1, 1, 10, 13), 2222, 1, True],\n",
    "    [dt.datetime(2020, 1, 2), np.nan, 2, False],\n",
    "    [dt.datetime(2020, 1, 2), np.inf, 3, True]\n",
    "]\n",
    "\n",
    "# Crie um DataFrame\n",
    "\n",
    "df = pd.DataFrame(\n",
    "    data=data,\n",
    "    columns=[\"Dates\", \"Floats\", \"Integers\", \"Booleans\"]\n",
    ")\n",
    "\n",
    "# Defina o nome do índice\n",
    "\n",
    "df.index.name = \"index\"\n",
    "\n",
    "# Exiba o DataFrame\n",
    "\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ec26b802-a716-4715-b7e7-2fb09559262f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_excel(\n",
    "    \"written_with_pandas.xlsx\",\n",
    "    sheet_name=\"Output\",\n",
    "    startrow=1,\n",
    "    startcol=1,\n",
    "    index=True,\n",
    "    header=True,\n",
    "    na_rep=\"<NA>\",\n",
    "    inf_rep=\"<INF>\"\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd23deae-80ee-4501-aa2f-2a2dbd6258f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Esse código salvará o DataFrame df em um arquivo Excel chamado \"written_with_pandas.xlsx\" com as seguintes configurações:\n",
    "\n",
    "# - sheet_name=\"Output\": O nome da planilha no arquivo Excel será \"Output\".\n",
    "# - startrow=1 e startcol=1: O DataFrame será escrito começando da segunda linha e segunda coluna da planilha.\n",
    "# - index=True: O índice do DataFrame será incluído no arquivo Excel.\n",
    "# - header=True: Os nomes das colunas do DataFrame serão incluídos no arquivo Excel.\n",
    "# - na_rep=\"<NA>\": Os valores ausentes (NaN) serão representados como \"<NA>\" no arquivo Excel.\n",
    "# - inf_rep=\"<INF>\": Os valores infinitos serão representados como \"<INF>\" no arquivo Excel.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7be5744b-28ba-4d8c-9e86-20bf1e62afad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Diretório atual: C:\\Users\\luist\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "# Salva o arquivo no Excel:\n",
    "\n",
    "df.to_excel(\"arquivo.xlsx\")\n",
    "\n",
    "# Verifica o diretório atual\n",
    "\n",
    "print(\"Diretório atual:\", os.getcwd())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e14c835-aa5f-476a-8efa-30e97b6ad07a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Trazer um arquivo do excel para o pandas:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5119be25-48c9-40a6-81da-29c96112f9ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\luist\n",
      "         NOME  ID-REGISTRO DATA-ADMISSÃO       CARGO  SALÁRIO  \\\n",
      "0     Rodrigo  755/-A-/877    2006-01-06    Auxiliar   1820.8   \n",
      "1      Agatha  611/-C-/683    2005-10-24    Analista   3182.1   \n",
      "2      Felipe  769/-B-/203    1997-05-08    Auxiliar   2177.6   \n",
      "3     Vitória  446/-C-/984    2015-05-08  Supervisor   4962.5   \n",
      "4    Benjamin  562/-B-/476    1998-07-23  Supervisor   5484.5   \n",
      "..        ...          ...           ...         ...      ...   \n",
      "194     Clara  538/-B-/189    1997-08-20    Auxiliar   1827.4   \n",
      "195  Isabelly  853/-A-/302    2015-09-18  Presidente  27618.0   \n",
      "196    Nicole  591/-C-/230    2008-12-17    Auxiliar   2055.8   \n",
      "197  Benjamin  539/-A-/940    2014-03-12  Assistente   2448.0   \n",
      "198   Cecília  447/-A-/120    2019-04-20  Assistente   2276.0   \n",
      "\n",
      "                CIDADE-ATUAÇÃO      LOJA  \n",
      "0             LOJA 004 - CEARÁ  LOJA 004  \n",
      "1    LOJA 003 - RIO DE JANEIRO  LOJA 003  \n",
      "2         LOJA 001 - SÃO PAULO  LOJA 001  \n",
      "3    LOJA 003 - RIO DE JANEIRO  LOJA 003  \n",
      "4         LOJA 001 - SÃO PAULO  LOJA 001  \n",
      "..                         ...       ...  \n",
      "194       LOJA 001 - SÃO PAULO  LOJA 001  \n",
      "195           LOJA 004 - CEARÁ  LOJA 004  \n",
      "196    LOJA 002 - MINAS GERAIS  LOJA 002  \n",
      "197  LOJA 003 - RIO DE JANEIRO  LOJA 003  \n",
      "198       LOJA 001 - SÃO PAULO  LOJA 001  \n",
      "\n",
      "[199 rows x 7 columns]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "# Verifica o diretório atual:\n",
    "\n",
    "print(os.getcwd())\n",
    "\n",
    "# Carrega o arquivo Excel:\n",
    "\n",
    "df = pd.read_excel('C:/Users/luist/OneDrive/Documentos/banco_de_dados.xlsx')\n",
    "\n",
    "# Exibe o DataFrame:\n",
    "\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74f4ccb5-d5d2-4118-b7e4-d366155ae4ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "# - Filtar os dados por cargo ou loja\n",
    "# - Agrupar os dados por cidade ou loja\n",
    "# - Calcular estatísticas descritivas, como média salarial por cargo\n",
    "# - Criar visualizações de dados, como gráficos de barras ou scatter plots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36dbeb80-5e09-4a62-b31d-56dddf8052c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        CARGO    SALÁRIO\n",
      "0    Analista   30871.20\n",
      "1  Assistente  117841.75\n",
      "2    Auxiliar  198310.00\n",
      "3         CEO  383720.00\n",
      "4     Diretor   81196.00\n",
      "5     Gerente  119895.00\n",
      "6  Presidente  123180.00\n",
      "7  Supervisor   96298.00\n"
     ]
    }
   ],
   "source": [
    "# Filtra os dados para mostrar o salário total por cargo\n",
    "\n",
    "salarios_por_cargo = df.groupby('CARGO')['SALÁRIO'].sum().reset_index()\n",
    "print(salarios_por_cargo)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6fe4c948-ce5c-49b1-babe-f935b35a8709",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Salário total: R$ 1151311.95\n"
     ]
    }
   ],
   "source": [
    "# Calcula o salário total de todos os funcionários:\n",
    "\n",
    "salario_total = df['SALÁRIO'].sum()\n",
    "print(f\"Salário total: R$ {salario_total:.2f}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f9adffb-8dd7-4550-805b-544482f6b1fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       LOJA      SALÁRIO\n",
      "0  LOJA 001  6605.120455\n",
      "1  LOJA 002  5602.750000\n",
      "2  LOJA 003  5159.727778\n",
      "3  LOJA 004  5913.973077\n"
     ]
    }
   ],
   "source": [
    "# Calcula a média salarial por loja:\n",
    "\n",
    "media_salarial_por_loja = df.groupby('LOJA')['SALÁRIO'].mean().reset_index()\n",
    "print(media_salarial_por_loja)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "bb102e73-81a0-422e-a02e-4fcd22bbcd06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       LOJA      SALÁRIO\n",
      "0  LOJA 001  6605.120455\n",
      "3  LOJA 004  5913.973077\n",
      "1  LOJA 002  5602.750000\n",
      "2  LOJA 003  5159.727778\n"
     ]
    }
   ],
   "source": [
    "# Caso queira ordenar os resultados por média salarial, pode adicionar o método sort_values():\n",
    "\n",
    "\n",
    "media_salarial_por_loja = df.groupby('LOJA')['SALÁRIO'].mean().reset_index().sort_values('SALÁRIO', ascending=False)\n",
    "print(media_salarial_por_loja)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f23a356f-137a-4e23-8529-92607eefe479",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Maior salário:\n",
      "NOME           Theo\n",
      "SALÁRIO    100710.0\n",
      "Name: 184, dtype: object\n",
      "\n",
      "Menor salário:\n",
      "NOME       Emanuel\n",
      "SALÁRIO     1808.2\n",
      "Name: 183, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# Encontra o maior salário com o nome correspondente:\n",
    "\n",
    "maior_salario = df.loc[df['SALÁRIO'].idxmax()]\n",
    "print(\"Maior salário:\")\n",
    "print(maior_salario[['NOME', 'SALÁRIO']])\n",
    "\n",
    "# Encontra o menor salário com o nome correspondente:\n",
    "\n",
    "menor_salario = df.loc[df['SALÁRIO'].idxmin()]\n",
    "print(\"\\nMenor salário:\")\n",
    "print(menor_salario[['NOME', 'SALÁRIO']])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b29c513-4623-421e-8315-476f57f282e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CIDADE-ATUAÇÃO\n",
      "LOJA 001 - SÃO PAULO         44\n",
      "LOJA 002 - MINAS GERAIS      49\n",
      "LOJA 003 - RIO DE JANEIRO    54\n",
      "LOJA 004 - CEARÁ             52\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Agrupa os dados por cidades:\n",
    "\n",
    "dados_por_cidade = df.groupby('CIDADE-ATUAÇÃO')\n",
    "print(dados_por_cidade.size())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "bf59493d-ae57-4792-b85a-92f3f4c8e706",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                           count         mean           std     min      25%  \\\n",
      "CIDADE-ATUAÇÃO                                                                 \n",
      "LOJA 001 - SÃO PAULO        44.0  6605.120455  15449.194617  1827.4  2069.00   \n",
      "LOJA 002 - MINAS GERAIS     49.0  5602.750000  13559.863451  1821.4  2139.20   \n",
      "LOJA 003 - RIO DE JANEIRO   54.0  5159.727778  14081.188904  1808.2  1876.40   \n",
      "LOJA 004 - CEARÁ            52.0  5913.973077  12927.697469  1808.6  2019.35   \n",
      "\n",
      "                               50%       75%       max  \n",
      "CIDADE-ATUAÇÃO                                          \n",
      "LOJA 001 - SÃO PAULO       2180.80  4594.625  100110.0  \n",
      "LOJA 002 - MINAS GERAIS    2342.75  2705.000   91510.0  \n",
      "LOJA 003 - RIO DE JANEIRO  2047.20  2621.375  100710.0  \n",
      "LOJA 004 - CEARÁ           2425.75  4755.625   91390.0  \n"
     ]
    }
   ],
   "source": [
    "# Agrupa os dados por cidades e calcula estatísticas descritivas:\n",
    "\n",
    "dados_por_cidade = df.groupby('CIDADE-ATUAÇÃO')['SALÁRIO'].describe()\n",
    "print(dados_por_cidade)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "95ea9add-900c-4737-8c46-dcbf155c7d0b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CARGO\n",
      "Analista       3087.120000\n",
      "Assistente     2507.271277\n",
      "Auxiliar       2003.131313\n",
      "CEO           95930.000000\n",
      "Diretor       20299.000000\n",
      "Gerente        9991.250000\n",
      "Presidente    30795.000000\n",
      "Supervisor     5068.315789\n",
      "Name: SALÁRIO, dtype: float64\n",
      "            count          mean          std       min        25%       50%  \\\n",
      "CARGO                                                                         \n",
      "Analista     10.0   3087.120000   160.673097   2855.10   2937.675   3152.25   \n",
      "Assistente   47.0   2507.271277   150.500017   2255.75   2372.625   2519.75   \n",
      "Auxiliar     99.0   2003.131313   122.493659   1808.20   1882.400   2020.20   \n",
      "CEO           4.0  95930.000000  5179.086148  91390.00  91480.000  95810.00   \n",
      "Diretor       4.0  20299.000000  1493.700996  18124.00  19963.000  20809.00   \n",
      "Gerente      12.0   9991.250000   539.458841   9168.00   9738.000   9983.00   \n",
      "Presidente    4.0  30795.000000  2184.103020  27618.00  30360.750  31500.00   \n",
      "Supervisor   19.0   5068.315789   336.632639   4511.00   4827.000   5169.00   \n",
      "\n",
      "                   75%       max  \n",
      "CARGO                             \n",
      "Analista      3202.350    3268.8  \n",
      "Assistente    2643.375    2717.5  \n",
      "Auxiliar      2117.500    2188.0  \n",
      "CEO         100260.000  100710.0  \n",
      "Diretor      21145.000   21454.0  \n",
      "Gerente      10263.000   10991.0  \n",
      "Presidente   31934.250   32562.0  \n",
      "Supervisor    5350.000    5484.5  \n"
     ]
    }
   ],
   "source": [
    "# Calcula a média salarial por cargo:\n",
    "\n",
    "media_salarial_por_cargo = df.groupby('CARGO')['SALÁRIO'].mean()\n",
    "print(media_salarial_por_cargo)\n",
    "\n",
    "# Calcula estatísticas descritivas para o salário por cargo:\n",
    "\n",
    "estatisticas_por_cargo = df.groupby('CARGO')['SALÁRIO'].describe()\n",
    "print(estatisticas_por_cargo)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f3ea59d-a4f3-45ae-865b-2cd422098cf0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA20AAAIiCAYAAABbiyDHAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAXDRJREFUeJzt3XlYFXX///HXkU3WI6KAGLnkrqmJpmhuuZZbqxaFy21mt6aZW3l3m7ZpqamVaWmaaRrV12zRIreyzDWMXHKp1NSELEUUMtbP7w9/zO0RRECUUZ+P6zrXxcy8Z+YzMzDnvJg5n3EYY4wAAAAAALZUqqQbAAAAAAA4P0IbAAAAANgYoQ0AAAAAbIzQBgAAAAA2RmgDAAAAABsjtAEAAACAjRHaAAAAAMDGCG0AAAAAYGOENgAAAACwMUIbAKDAHnjgAdWsWVN//fVXSTcFAIBrBqENAK5y8+fPl8PhkMPh0Ndff51rujFG1apVk8PhUJs2bc67nDfeeEOrV69WbGysypUrV6B1V65cWX379rWGv/766/O2o6iOHTumMWPGqE6dOvL19ZXT6VStWrUUHR2tbdu2FXp5Bw4ckMPh0Pz584utjdLFbful2G+X2rZt29SvXz9VqVJFpUuXlp+fnxo1aqRJkybp+PHjJd08ALiiuJd0AwAAl4e/v7/mzp2bK5itXbtWv/76q/z9/c8779atWzV27Fh9+eWXqlKlSpHb0KhRI23YsEF16tQp8jLOlpKSombNmiklJUWjRo1SgwYNdPr0ae3du1cfffSR4uPjVb9+/WJZ18Uq7m23szlz5mjQoEGqWbOmRo0apTp16igjI0Pff/+93njjDW3YsEFLly4t6WYCwBWD0AYA14hevXpp0aJFev311xUQEGCNnzt3riIjI3Xy5MnzztuoUSP9+eefF92GgIAANWvW7KKXk+PDDz/UL7/8ojVr1qht27Yu04YPH67s7OxiW1dRZWRkyOFwFPu2l6S///5bPj4+eU7bsGGD/v3vf6tDhw76+OOP5eXlZU3r0KGDRowYodjY2EveDgC4mnB7JABcI+6//35J0nvvvWeNS05O1pIlS/Svf/0rz3nS09P1/PPPq1atWvLy8lL58uXVr1+/XAEuIyNDo0ePVmhoqHx8fHTLLbdo8+bNuZaX121+33//ve677z5VrlxZ3t7eqly5su6//3799ttvF9ymY8eOSZIqVKiQ5/RSpf73NvfLL7+oX79+ql69unx8fFSxYkV169ZN27dvv+B6CjpvzvYtXLhQI0aMUMWKFeXl5aVffvml2Lc9Lzm3wq5cuVL9+vVT2bJl5evrq27dumnfvn256ufNm6cGDRqodOnSKlu2rO68807t2rXLpaZv377y8/PT9u3b1bFjR/n7+6tdu3bnbcOECRPkcDg0e/Zsl8CWw9PTU927d7eG33//fXXs2FEVKlSQt7e3ateurSeffFKpqakFbseJEyfUv39/lS1bVn5+furSpYv27dsnh8Oh8ePHuyxn3bp1ateunfz9/eXj46PmzZtr+fLlF9y3AFCSCG0AcI0ICAjQPffco3nz5lnj3nvvPZUqVUq9evXKVZ+dna0ePXroxRdfVFRUlJYvX64XX3xRK1euVJs2bXT69GmrdsCAAZoyZYp69+6tTz75RHfffbfuuusuJSUlXbBdBw4cUM2aNTV9+nR9+eWXeumll5SQkKAmTZpcsMOTyMhISVLv3r318ccfWyEuL0eOHFFQUJBefPFFxcbG6vXXX5e7u7uaNm2qPXv25Luews47ZswYHTx4UG+88YY+++wzBQcHF/u256d///4qVaqUFi9erOnTp2vz5s1q06aNTpw4YdVMnDhR/fv3V926dfXRRx/plVde0bZt2xQZGamff/7ZZXnp6enq3r27br31Vn3yySd65pln8lxvVlaW1qxZo4iICIWHhxeorT///LNuv/12zZ07V7GxsRo2bJg++OADdevWLVdtXu3Izs5Wt27dtHjxYj3xxBNaunSpmjZtqs6dO+eaf+3atbr11luVnJysuXPn6r333pO/v7+6deum999/v0DtBYASYQAAV7W3337bSDJbtmwxX331lZFkduzYYYwxpkmTJqZv377GGGPq1q1rWrdubc333nvvGUlmyZIlLsvbsmWLkWRmzpxpjDFm165dRpJ5/PHHXeoWLVpkJJk+ffpY43LW/9VXX523vZmZmSYlJcX4+vqaV1555YLb9+yzzxpPT08jyUgyVapUMY888oj58ccf850vMzPTpKenm+rVq7u0ff/+/UaSefvttws9b872tWrVKtc8F7PtBZnXmP8d6zvvvNNl/HfffWckmeeff94YY0xSUpLx9vY2t99+u0vdwYMHjZeXl4mKirLG9enTx0gy8+bNy3fdxhiTmJhoJJn77rvvgrV5yc7ONhkZGWbt2rVGkssxPF87li9fbiSZWbNmuYyfOHGikWTGjRtnjWvWrJkJDg42p06dssZlZmaaevXqmeuuu85kZ2cXqd0AcKlxpQ0AriGtW7fWDTfcoHnz5mn79u3asmXLeW+NXLZsmcqUKaNu3bopMzPTejVs2FChoaHWbX5fffWVpDOPAzhbz5495e5+4a9Op6Sk6IknnlC1atXk7u4ud3d3+fn5KTU1NdetenkZO3asDh48qHnz5mngwIHy8/PTG2+8oYiICJdbQTMzMzVhwgTVqVNHnp6ecnd3l6enp37++ecLrqew8959990XbHdxbPv5nHssmjdvrkqVKlnHasOGDTp9+rRLz56SFB4erltvvVWrV6/OtcyCblNh7du3T1FRUQoNDZWbm5s8PDzUunVrSSrQvl27dq2kM79vZ8u5HThHamqqNm3apHvuuUd+fn7WeDc3N0VHR+vw4cMXvOIKACWFjkgA4BricDjUr18/vfrqq/rnn39Uo0YNtWzZMs/aP/74QydOnJCnp2ee03Nu38u5JTE0NNRluru7u4KCgi7YpqioKK1evVpjx45VkyZNFBAQIIfDodtvv93lFsz8hISEqF+/furXr58k6ZtvvtFtt92mxx57zPrwPnz4cL3++ut64okn1Lp1awUGBqpUqVJ66KGHLriews57vu/YXYptz8u5xyJnXM6xyu+7gGFhYVq5cqXLOB8fH5fOa86nXLly8vHx0f79+wvUzpSUFLVs2VKlS5fW888/rxo1asjHx0eHDh3SXXfdlWsf5NWOY8eOyd3dXWXLlnUZHxIS4jKclJQkY8x5tzlnWQBgR4Q2ALjG9O3bV08//bTeeOMNvfDCC+etK1eunIKCgs7b01/OIwJyglliYqIqVqxoTc/MzLzgh+Dk5GQtW7ZM48aN05NPPmmNT0tLu6hnebVq1UodO3bUxx9/rKNHjyo4OFjvvvuuevfurQkTJrjU/vXXXypTpky+yyvsvA6H44JtvFTbLp05FnmNq1atmqT/HbOEhIRcdUeOHMn1HL6CbI905qpVu3bt9MUXX+jw4cO67rrr8q1fs2aNjhw5oq+//tq6uibJ5bt3F2pHUFCQMjMzdfz4cZfgdu4+yAna59tmSQV+/iAAXG7cHgkA15iKFStq1KhR6tatm/r06XPeuq5du+rYsWPKyspS48aNc71q1qwpSdZz3xYtWuQy/wcffKDMzMx82+JwOGSMydXL4FtvvaWsrKwLbssff/yRZ7f+WVlZ+vnnn+Xj42OFKofDkWs9y5cv1++//37B9VzMvPkt82K2PT/nHov169frt99+s45VZGSkvL299e6777rUHT58WGvWrMm3d8gLGTNmjIwxGjBggNLT03NNz8jI0GeffSbpfyHs3H3w5ptvFnh9OWHv3I5EYmJiXIZ9fX3VtGlTffTRRy5X8LKzs/Xuu+/quuuuU40aNQq8XgC4nLjSBgDXoBdffPGCNffdd58WLVqk22+/XY899phuvvlmeXh46PDhw/rqq6/Uo0cP3Xnnnapdu7YefPBBTZ8+XR4eHmrfvr127NihKVOmXPCWuoCAALVq1UqTJ09WuXLlVLlyZa1du1Zz58694NUvSVq4cKHefPNNRUVFqUmTJnI6nTp8+LDeeust7dy5U08//bR1e2fXrl01f/581apVS/Xr11dcXJwmT558watBFzvvpdr2/Hz//fd66KGHdO+99+rQoUN66qmnVLFiRQ0aNEiSVKZMGY0dO1b/+c9/1Lt3b91///06duyYnnnmGZUuXVrjxo0r8rojIyM1a9YsDRo0SBEREfr3v/+tunXrKiMjQz/88INmz56tevXqqVu3bmrevLkCAwP1yCOPaNy4cfLw8NCiRYv0448/Fnh9nTt3VosWLTRixAidPHlSERER2rBhgxYsWCDJ9bEPEydOVIcOHdS2bVuNHDlSnp6emjlzpnbs2KH33nuvwFcUAeByI7QBAPLk5uamTz/9VK+88ooWLlyoiRMnyt3dXdddd51at26tG2+80aqdO3euQkJCNH/+fL366qtq2LChlixZovvuu++C61m8eLEee+wxjR49WpmZmWrRooVWrlypLl26XHDeLl26KDExUZ9//rlmzZqlpKQk+fv7q379+lq4cKEefPBBq/aVV16Rh4eHJk6cqJSUFDVq1EgfffSR/vvf/15wPRcz76Xa9vzMnTtXCxcu1H333ae0tDS1bdtWr7zyisvtg2PGjFFwcLBeffVVvf/++/L29labNm00YcIEVa9e/aLWP2DAAN18882aNm2aXnrpJSUmJsrDw0M1atRQVFSUHn30UUlnbm1cvny5RowYoQcffFC+vr7q0aOH3n//fTVq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MP30008KDAzUF198oUOHDqlly5a69957L2mDAQAAAOBaUqDQNmLECDVp0kRt27aVJO3atUv9+vWTJLm7u+v06dPy9/fXc889p5deeunStRYAAAAArjEFuj3S4XBo7NixVmjz9fW1vsdWoUIF/frrr6pUqZIcDof++uuvS9daAAAAALjGFKr3yFtuuUWS1KxZM61bt06SdPvtt2vw4MGaMGGC+vXrp2bNmhV/KwEAAADgGlWk3iOnTp2qU6dOSZKefPJJHT9+XDExMbrhhhs0bdq0Ym0gAAAAAFzLihTaqlatav1cunRpvfrqq8XWIAAAAADA//BwbQAAAACwsQJfaQsMDLSe03Yhx48fL3KDAAAAAAD/U+DQNn369EvYDAAAAABAXgoc2vr06XMp2wEAAAAAyEOROiI52+nTp5WRkeEyLiAg4GIXCwAAAABQETsiSU1N1aOPPqrg4GD5+fkpMDDQ5QUAAAAAKB5FCm2jR4/WmjVrNHPmTHl5eemtt97SM888o7CwMC1YsKC42wgAAAAA16wi3R752WefacGCBWrTpo3+9a9/qWXLlqpWrZoqVaqkRYsW6YEHHijudgIAAADANalIV9qOHz+uKlWqSDrz/bWcLv5vueUWffPNN8XXOgAAAAC4xhUptFWtWlUHDhyQJNWpU0cffPCBpDNX4MqUKVNcbQMAAACAa16RQlu/fv30448/SpLGjBljfbft8ccf16hRo4q1gQAAAABwLSvSd9oef/xx6+e2bdtq9+7d+v7773XDDTeoQYMGxdY4AAAAALjWFepK26ZNm/TFF1+4jFuwYIFat26tRx55RK+//rrS0tKKtYEAAAAAcC0rVGgbP368tm3bZg1v375d/fv3V/v27TVmzBh99tlnmjhxYrE3EgAAAACuVYUKbfHx8WrXrp01HBMTo6ZNm2rOnDl6/PHH9eqrr1qdkgAAAAAALl6hQltSUpJCQkKs4bVr16pz587WcJMmTXTo0KHiax0AAAAAXOMKFdpCQkK0f/9+SVJ6erq2bt2qyMhIa/qpU6fk4eFRvC0EAAAAgGtYoUJb586d9eSTT+rbb7/VmDFj5OPjo5YtW1rTt23bphtuuKHYGwkAAAAA16pCdfn//PPP66677lLr1q3l5+end955R56entb0efPmqWPHjsXeSAAAAAC4VhUqtJUvX17ffvutkpOT5efnJzc3N5fpH374ofz8/Iq1gQAAAABwLSvSw7WdTmee48uWLXtRjQEAAAAAuCrUd9oAAAAAAJcXoQ0AAAAAbIzQBgAAAAA2RmgDAAAAABsjtAEAAACAjRHaAAAAAMDGCG0AAAAAYGOENgAAAACwMUIbAAAAANgYoQ0AAAAAbIzQBgAAAAA2RmgDAAAAABsjtAEAAACAjRHaAAAAAMDGCG0AAAAAYGOENgAAAACwMUIbAAAAANgYoQ0AAAAAbIzQBgAAAAA2RmgDAAAAABsjtAEAAACAjRHaAAAAAMDGCG0AAAAAYGOENgAAAACwMUIbAAAAANgYoQ0AAAAAbOyKCm0TJ06Uw+HQsGHDrHHGGI0fP15hYWHy9vZWmzZttHPnTpf50tLSNGTIEJUrV06+vr7q3r27Dh8+7FKTlJSk6OhoOZ1OOZ1ORUdH68SJEy41Bw8eVLdu3eTr66ty5cpp6NChSk9Pv1SbCwAAAABXTmjbsmWLZs+erfr167uMnzRpkqZOnaoZM2Zoy5YtCg0NVYcOHXTq1CmrZtiwYVq6dKliYmK0bt06paSkqGvXrsrKyrJqoqKiFB8fr9jYWMXGxio+Pl7R0dHW9KysLHXp0kWpqalat26dYmJitGTJEo0YMeLSbzwAAACAa9YVEdpSUlL0wAMPaM6cOQoMDLTGG2M0ffp0PfXUU7rrrrtUr149vfPOO/r777+1ePFiSVJycrLmzp2rl19+We3bt9dNN92kd999V9u3b9eqVaskSbt27VJsbKzeeustRUZGKjIyUnPmzNGyZcu0Z88eSdKKFSv0008/6d1339VNN92k9u3b6+WXX9acOXN08uTJ87Y9LS1NJ0+edHkBAAAAQEFdEaFt8ODB6tKli9q3b+8yfv/+/UpMTFTHjh2tcV5eXmrdurXWr18vSYqLi1NGRoZLTVhYmOrVq2fVbNiwQU6nU02bNrVqmjVrJqfT6VJTr149hYWFWTWdOnVSWlqa4uLiztv2iRMnWrdcOp1OhYeHX8SeAAAAAHCtsX1oi4mJ0datWzVx4sRc0xITEyVJISEhLuNDQkKsaYmJifL09HS5QpdXTXBwcK7lBwcHu9Scu57AwEB5enpaNXkZM2aMkpOTrdehQ4cutMkAAAAAYHEv6Qbk59ChQ3rssce0YsUKlS5d+rx1DofDZdgYk2vcuc6tyau+KDXn8vLykpeXV75tAQAAAIDzsfWVtri4OB09elQRERFyd3eXu7u71q5dq1dffVXu7u7Wla9zr3QdPXrUmhYaGqr09HQlJSXlW/PHH3/kWv+ff/7pUnPuepKSkpSRkZHrChwAAAAAFBdbh7Z27dpp+/btio+Pt16NGzfWAw88oPj4eFWtWlWhoaFauXKlNU96errWrl2r5s2bS5IiIiLk4eHhUpOQkKAdO3ZYNZGRkUpOTtbmzZutmk2bNik5OdmlZseOHUpISLBqVqxYIS8vL0VERFzS/QAAAADg2mXr2yP9/f1Vr149l3G+vr4KCgqyxg8bNkwTJkxQ9erVVb16dU2YMEE+Pj6KioqSJDmdTvXv318jRoxQUFCQypYtq5EjR+rGG2+0OjapXbu2OnfurAEDBujNN9+UJD388MPq2rWratasKUnq2LGj6tSpo+joaE2ePFnHjx/XyJEjNWDAAAUEBFyuXQIAAADgGmPr0FYQo0eP1unTpzVo0CAlJSWpadOmWrFihfz9/a2aadOmyd3dXT179tTp06fVrl07zZ8/X25ublbNokWLNHToUKuXye7du2vGjBnWdDc3Ny1fvlyDBg1SixYt5O3traioKE2ZMuXybSwAAACAa47DGGNKuhHXkpMnT8rpdCo5OZkrdABsL2LUgpJuwhUnbnLvkm4CAOAKUdBsYOvvtAEAAADAtY7QBgAAAAA2RmgDAAAAABsjtAEAAACAjRHaAAAAAMDGCG0AAAAAYGOENgAAAACwMUIbAAAAANgYoQ0AAAAAbIzQBgAAAAA2RmgDAAAAABsjtAEAAACAjRHaAAAAAMDGCG0AAAAAYGOENgAAAACwMUIbAAAAANgYoQ0AAAAAbIzQBgAAAAA2RmgDAAAAABsjtAEAAACAjRHaAAAAAMDGCG0AAAAAYGOENgAAAACwMUIbAAAAANiYe0k3AAAAALiSGGOUmppqDfv6+srhcJRgi3C1I7QBAAAAhZCamqoePXpYw5988on8/PxKsEW42nF7JAAAAADYGKENAAAAAGyM0AYAAAAANkZoAwAAAAAbI7QBAAAAgI0R2gAAAADAxghtAAAAAGBjPKcNAAAAthUxakFJNyEXR2a6nGcNtxkbI+PuWWLtyUvc5N4l3QQUI660AQAAAICNEdoAAAAAwMYIbQAAAABgY4Q2AAAAALAxQhsAAAAA2BihDQAAAABsjNAGAAAAADZGaAMAAAAAGyO0AQAAAICNEdoAAAAAwMYIbQAAAABgY+4l3QAAAADgSmLcPJRc/36XYeBSIrQBAAAAheFwyLh7lnQrcA3h9kgAAAAAsDFCGwAAAADYGKENAAAAAGyM0AYAAAAANkZoAwAAAAAbI7QBAAAAgI0R2gAAAADAxghtAAAAAGBjhDYAAAAAsDFCGwAAAADYGKENAAAAAGyM0AYAAAAANkZoAwAAAAAbI7QBAAAAgI0R2gAAAADAxghtAAAAAGBjhDYAAAAAsDFCGwAAAADYGKENAAAAAGyM0AYAAAAANkZoAwAAAAAbI7QBAAAAgI0R2gAAAADAxghtAAAAAGBjhDYAAAAAsDFCGwAAAADYmHtJNwAAAAAACsMYo9TUVGvY19dXDoejBFt0aRHaAAAAAFxRUlNT1aNHD2v4k08+kZ+fXwm26NLi9kgAAAAAsDFbh7aJEyeqSZMm8vf3V3BwsO644w7t2bPHpcYYo/HjxyssLEze3t5q06aNdu7c6VKTlpamIUOGqFy5cvL19VX37t11+PBhl5qkpCRFR0fL6XTK6XQqOjpaJ06ccKk5ePCgunXrJl9fX5UrV05Dhw5Venr6Jdl2AAAAAJBsHtrWrl2rwYMHa+PGjVq5cqUyMzPVsWNHl/tXJ02apKlTp2rGjBnasmWLQkND1aFDB506dcqqGTZsmJYuXaqYmBitW7dOKSkp6tq1q7KysqyaqKgoxcfHKzY2VrGxsYqPj1d0dLQ1PSsrS126dFFqaqrWrVunmJgYLVmyRCNGjLg8OwMAAADANcnW32mLjY11GX777bcVHBysuLg4tWrVSsYYTZ8+XU899ZTuuusuSdI777yjkJAQLV68WAMHDlRycrLmzp2rhQsXqn379pKkd999V+Hh4Vq1apU6deqkXbt2KTY2Vhs3blTTpk0lSXPmzFFkZKT27NmjmjVrasWKFfrpp5906NAhhYWFSZJefvll9e3bVy+88IICAgIu454BAAAAcK2wdWg7V3JysiSpbNmykqT9+/crMTFRHTt2tGq8vLzUunVrrV+/XgMHDlRcXJwyMjJcasLCwlSvXj2tX79enTp10oYNG+R0Oq3AJknNmjWT0+nU+vXrVbNmTW3YsEH16tWzApskderUSWlpaYqLi1Pbtm3zbHNaWprS0tKs4ZMnTxbPzgAAAAAug4hRC0q6Cbk4MtPlPGu4zdgYGXfPEmtPXuIm9y62Zdn69sizGWM0fPhw3XLLLapXr54kKTExUZIUEhLiUhsSEmJNS0xMlKenpwIDA/OtCQ4OzrXO4OBgl5pz1xMYGChPT0+rJi8TJ060vifndDoVHh5emM0GAAAAcI27YkLbo48+qm3btum9997LNe3cZzIYYy74nIZza/KqL0rNucaMGaPk5GTrdejQoXzbBQAAAABnuyJC25AhQ/Tpp5/qq6++0nXXXWeNDw0NlaRcV7qOHj1qXRULDQ1Venq6kpKS8q35448/cq33zz//dKk5dz1JSUnKyMjIdQXubF5eXgoICHB5AQAAAEBB2Tq0GWP06KOP6qOPPtKaNWtUpUoVl+lVqlRRaGioVq5caY1LT0/X2rVr1bx5c0lSRESEPDw8XGoSEhK0Y8cOqyYyMlLJycnavHmzVbNp0yYlJye71OzYsUMJCQlWzYoVK+Tl5aWIiIji33gAAAAAkM07Ihk8eLAWL16sTz75RP7+/taVLqfTKW9vbzkcDg0bNkwTJkxQ9erVVb16dU2YMEE+Pj6Kioqyavv3768RI0YoKChIZcuW1ciRI3XjjTdavUnWrl1bnTt31oABA/Tmm29Kkh5++GF17dpVNWvWlCR17NhRderUUXR0tCZPnqzjx49r5MiRGjBgAFfPAAAAAFwytg5ts2bNkiS1adPGZfzbb7+tvn37SpJGjx6t06dPa9CgQUpKSlLTpk21YsUK+fv7W/XTpk2Tu7u7evbsqdOnT6tdu3aaP3++3NzcrJpFixZp6NChVi+T3bt314wZM6zpbm5uWr58uQYNGqQWLVrI29tbUVFRmjJlyiXaegAAAACweWgzxlywxuFwaPz48Ro/fvx5a0qXLq3XXntNr7322nlrypYtq3fffTffdV1//fVatmzZBdsEAAAAAMXF1qENAAAAAM5l3DyUXP9+l+GrGaENAAAAwJXF4bDdw7QvJVv3HgkAAAAA1zpCGwAAAADYGKENAAAAAGyM0AYAAAAANkZoAwAAAAAbI7QBAAAAgI0R2gAAAADAxghtAAAAAGBjhDYAAAAAsDFCGwAAAADYGKENAAAAAGyM0AYAAAAANkZoAwAAAAAbI7QBAAAAgI0R2gAAAADAxghtAAAAAGBjhDYAAAAAsDFCGwAAAADYGKENAAAAAGyM0AYAAAAANkZoAwAAAAAbI7QBAAAAgI0R2gAAAADAxghtAAAAAGBjhDYAAAAAsDFCGwAAAADYGKENAAAAAGyM0AYAAAAANkZoAwAAAAAbI7QBAAAAgI0R2gAAAADAxghtAAAAAGBj7iXdAAAAABScMUapqanWsK+vrxwORwm2CMClRmgDAAC4gqSmpqpHjx7W8CeffCI/P78SbBGAS43bIwEAAADAxrjSBgAAkI+IUQtKugkuHJnpcp413GZsjIy7Z4m1Jy9xk3uXdBOAqwpX2gAAAADAxghtAAAAAGBj3B4JAABwBTFuHkquf7/LMICrG6ENAADgSuJw2O47bAAuLW6PBAAAAAAbI7QBAAAAgI0R2gAAAADAxghtAAAAAGBjhDYAAAAAsDFCGwAAAADYGKENAAAAAGyM0AYAAAAANkZoAwAAAAAbI7QBAAAAgI0R2gAAAADAxghtAAAAAGBjhDYAAAAAsDFCGwAAAADYmHtJNwAAriTGGKWmplrDvr6+cjgcJdgiAABwtSO0AUAhpKamqkePHtbwJ598Ij8/vxJsEQAAuNpxeyQAAAAA2BhX2gDYVsSoBSXdhFwcmelynjXcZmyMjLtnibXnXHGTe5d0EwAAQDHjShsAAAAA2BhX2gCgEIybh5Lr3+8yDAAAcCkR2gCgMBwOW90OCQAArn7cHgkAAAAANkZoAwAAAAAb4/ZI4ArCg50BAACuPYQ24ArCg50BAACuPYQ24Dx4RljR8JwwAACA4sV32gAAAADAxghtAAAAAGBj3B4JXEF4sDNw7bHjrdp2x23aAK42hDbgSsKDnQEAAK45hDab4j+rRcN/VwEAAHC14TttAAAAAGBjhDYAAAAAsDFCGwAAAADYGKENAAAAAGyM0FYEM2fOVJUqVVS6dGlFRETo22+/LekmAQAAALhKEdoK6f3339ewYcP01FNP6YcfflDLli1122236eDBgyXdNAAAAABXIUJbIU2dOlX9+/fXQw89pNq1a2v69OkKDw/XrFmzSrppAAAAAK5CPKetENLT0xUXF6cnn3zSZXzHjh21fv36POdJS0tTWlqaNZycnCxJOnnyZL7ryko7fZGtvTZdaL8WBsegaDgGJas497/EMSgKjkHJ4xiUPN4LSh7HoOQV5Bjk1Bhj8q1zmAtVwHLkyBFVrFhR3333nZo3b26NnzBhgt555x3t2bMn1zzjx4/XM888czmbCQAAAOAKcujQIV133XXnnc6VtiJwOBwuw8aYXONyjBkzRsOHD7eGs7Ozdfz4cQUFBZ13Hjs7efKkwsPDdejQIQUEBJR0c65JHIOSxzEoeRyDksX+L3kcg5LHMSh5V8MxMMbo1KlTCgsLy7eO0FYI5cqVk5ubmxITE13GHz16VCEhIXnO4+XlJS8vL5dxZcqUuVRNvGwCAgKu2D+OqwXHoORxDEoex6Bksf9LHseg5HEMSt6VfgycTucFa+iIpBA8PT0VERGhlStXuoxfuXKly+2SAAAAAFBcuNJWSMOHD1d0dLQaN26syMhIzZ49WwcPHtQjjzxS0k0DAAAAcBUitBVSr169dOzYMT377LNKSEhQvXr19Pnnn6tSpUol3bTLwsvLS+PGjct1yycuH45ByeMYlDyOQcli/5c8jkHJ4xiUvGvpGNB7JAAAAADYGN9pAwAAAAAbI7QBAAAAgI0R2gAAAADAxghtKLSvv/5aDodDJ06ckCTNnz/f5dlz48ePV8OGDUukbdeCypUra/r06daww+HQxx9/XGLtQcGde+wAu+F8AuR27uecvPDZp3hwDjo/QttVav369XJzc1Pnzp2LfdnNmzdXQkLCeR8EOHLkSK1evbrY13uluJT7Pi8JCQm67bbbClR7pZ8Mjx49qoEDB+r666+Xl5eXQkND1alTJ23YsKGkm1YgW7Zs0cMPP1zSzbCtxMREDRkyRFWrVpWXl5fCw8PVrVs363xSuXJlORyOXK8XX3zRZTnvvPOObr75Zvn6+srf31+tWrXSsmXLSmKTLqlLca6xw/nk3H8MXqkSExP12GOPqVq1aipdurRCQkJ0yy236I033tDff/9d0s1TmzZtNGzYsJJuRpH07dvX+vv38PBQ1apVNXLkSKWmpl6S9fXq1Ut79+69JMvOT0HC4pXi3GMWEhKiDh06aN68ecrOzrbqCnMOOp8DBw7I4XAoPj7+IlttL4S2q9S8efM0ZMgQrVu3TgcPHizWZXt6eio0NFQOhyPP6X5+fgoKCrqodWRkZFzU/CXpUu77vISGhl4TXd1K0t13360ff/xR77zzjvbu3atPP/1Ubdq00fHjx0u0Xenp6QWqK1++vHx8fC5JG7Kyslze+K40Bw4cUEREhNasWaNJkyZp+/btio2NVdu2bTV48GCrLudxK2e/hgwZYk0fOXKkBg4cqJ49e+rHH3/U5s2b1bJlS/Xo0UMzZswoiU27ZC7FueZaOp9cSvv27dNNN92kFStWaMKECfrhhx+0atUqPf744/rss8+0atWqIi33Sn5vLG6dO3dWQkKC9u3bp+eff14zZ87UyJEjc9UVxz7z9vZWcHDwRS/nWpdzzA4cOKAvvvhCbdu21WOPPaauXbsqMzNT0oXPQZf7b8BWf3MGV52UlBTj7+9vdu/ebXr16mWeeeYZa9rbb79tnE6nS/3SpUtNzq9Cdna2adeunenUqZPJzs42xhiTlJRkwsPDzX/+8x9jjDFfffWVkWSSkpLyXOa4ceNMgwYNrOHNmzeb9u3bm6CgIBMQEGBatWpl4uLiXNogycyaNct0797d+Pj4mKeffrqY9sblld++z9lvq1atMhEREcbb29tERkaa3bt3WzW//PKL6d69uwkODja+vr6mcePGZuXKlS7rqFSpkpk2bZo1LMksXbrUGGNMWlqaGTx4sAkNDTVeXl6mUqVKZsKECdZ8kqxXpUqVCrxOO0hKSjKSzNdff53n9P379xtJ5ocffsg1z1dffWWM+d8xWLZsmalfv77x8vIyN998s9m2bZvLsr777jvTsmVLU7p0aXPdddeZIUOGmJSUFGt6pUqVzHPPPWf69OljAgICTO/evU2zZs3ME0884bKco0ePGnd3d7NmzRprvrOP3bhx40x4eLjx9PQ0FSpUMEOGDLGmHT9+3ERHR5syZcoYb29v07lzZ7N3715res7f3WeffWZq165t3NzczL59+wq1T+3ktttuMxUrVnTZzzlyzjXn7r9zbdiwwUgyr776aq5pw4cPNx4eHubgwYPF1eQSld+55vjx4yYqKsqUK1fOlC5d2lSrVs3MmzfPGJP/OcKYiz+fGGPMp59+aho1amS8vLxMlSpVzPjx401GRobLOubMmWPuuOMO4+3tbapVq2Y++eQTY8z//o7PfvXp08cYc+b96aWXXjJVqlQxpUuXNvXr1zcffvjhpdi9F61Tp07muuuuy/P32Rhjvb+eOHHCDBgwwJQvX974+/ubtm3bmvj4eKsu5/107ty5pkqVKsbhcJjs7OwCz7dgwQJTqVIlExAQYHr16mVOnjxpjDGmT58+ufbz/v37jTHG7Ny509x2223G19fXBAcHmwcffND8+eefl2hPFU2fPn1Mjx49XMY99NBDJjQ0tMj7LD4+3rRp08b4+fkZf39/06hRI7NlyxZjTN6fnSZOnGiCg4ONn5+f+de//mWeeOIJl88+xhgzb948U6tWLePl5WVq1qxpXn/9dWtazu/6kiVLTJs2bYy3t7epX7++Wb9+vTHmf+9XZ7/GjRtnjDnztzlq1CgTFhZmfHx8zM0332y9z9lVXsfMGGNWr15tnROMcT0H5eyj999/37Ru3dp4eXlZ57L89u25+61169bGGGOysrLMM888YypWrGg8PT1NgwYNzBdffGHNl9/67IDQdhWaO3euady4sTHGmM8++8xUrlzZeoO4UGgzxpjDhw+bwMBAM336dGOMMb169TKNGzc26enpxpjCh7bVq1ebhQsXmp9++sn89NNPpn///iYkJMR68zDmzB9YcHCwmTt3rvn111/NgQMHimt3XFb57fuc/da0aVPz9ddfm507d5qWLVua5s2bW/PHx8ebN954w2zbts3s3bvXPPXUU6Z06dLmt99+s2ryC22TJ0824eHh5ptvvjEHDhww3377rVm8eLEx5kyAkGTefvttk5CQYI4ePVrgddpBRkaG8fPzM8OGDTP//PNPrumFCW21a9c2K1asMNu2bTNdu3Y1lStXtn6/t23bZvz8/My0adPM3r17zXfffWduuukm07dvX2u5OR+CJk+ebH7++Wfz888/m9dee81cf/311vE2xpjXXnvNVKxY0WRlZVnz5Ry7Dz/80AQEBJjPP//c/Pbbb2bTpk1m9uzZ1rzdu3c3tWvXNt98842Jj483nTp1MtWqVbPa+fbbbxsPDw/TvHlz891335ndu3ef9wOi3R07dsw4HA6X8JCXC4W2oUOHGj8/P5OWlpZr2u+//24k5Tv/lSS/c83gwYNNw4YNzZYtW8z+/fvNypUrzaeffmqMyf8cYczFn09iY2NNQECAmT9/vvn111/NihUrTOXKlc348eNd1nHdddeZxYsXm59//tk6bseOHTOZmZlmyZIlRpLZs2ePSUhIMCdOnDDGGPOf//zH1KpVy8TGxppff/3VvP3228bLy+u8/8gpKX/99ZdxOBxm4sSJ+dZlZ2ebFi1amG7dupktW7aYvXv3mhEjRpigoCBz7NgxY8yZ91NfX1/TqVMns3XrVvPjjz8WeD4/Pz9z1113me3bt5tvvvnGhIaGWv98PXHihImMjDQDBgwwCQkJJiEhwWRmZpojR46YcuXKmTFjxphdu3aZrVu3mg4dOpi2bdte2p1WSHkFgCFDhpigoKAi77O6deuaBx980Ozatcvs3bvXfPDBB1aoO/dzzvvvv288PT3NnDlzzO7du81TTz1l/P39XT77zJ4921SoUMEsWbLE7Nu3zyxZssSULVvWzJ8/3xjzv/esWrVqmWXLlpk9e/aYe+65x1SqVMlkZGSYtLQ0M336dBMQEGAdo1OnThljjImKijLNmzc333zzjfnll1/M5MmTjZeXl8s/9uzmfKHNGGMaNGhgbrvtNmNM3qGtcuXK1n78/fffL7hvN2/ebP2TPCEhwTrGU6dONQEBAea9994zu3fvNqNHjzYeHh7Wfjvf+uyC0HYVat68uRW4MjIyTLly5awrJwUJbcYY88EHHxgvLy8zZswY4+PjY/bs2WNNK2xoO1dmZqbx9/c3n332mTVOkhk2bFgRttZe8tv3Z19py7F8+XIjyZw+ffq8y6xTp4557bXXrOH8QtuQIUPMrbfe6hIcznZ2bX7OXadd/N///Z8JDAw0pUuXNs2bNzdjxowxP/74ozGmcKEtJibGqjl27Jjx9vY277//vjHGmOjoaPPwww+7rPfbb781pUqVso5TpUqVzB133OFSk3NV7ZtvvrHGRUZGmlGjRlnDZx+7l19+2dSoUcMKYWfbu3evkWS+++47a9xff/1lvL29zQcffGCMOfN3J8nlP8VXqk2bNhlJ5qOPPsq3rlKlSsbT09P4+vq6vHKOb+fOnfM99zidTvPvf/+7GFtecvI713Tr1s3069cvz/kKc44oyvmkZcuWucL3woULTYUKFVzm++9//2sNp6SkGIfDYf3H+9z3mJya0qVLW1chcvTv39/cf//9ebavpGzcuDHP3+egoCDrd3b06NFm9erVJiAgINc/oW644Qbz5ptvGmPOvJ96eHhYodgYU+D5fHx8XP45OmrUKNO0aVNruHXr1uaxxx5zWcbYsWNNx44dXcYdOnTICtF2cW4A2LRpkwkKCjI9e/Ys8j7z9/e3PvSf69zPOZGRkeaRRx5xqWnatKnL+Sc8PNzlHyLGGPPcc8+ZyMhIY8z/3rPeeusta/rOnTuNJLNr164812vMmbtjHA5HrjDRrl07M2bMmDzbbwf5hbZevXqZ2rVrG2PyDm0557ocBd23Z38eMMaYsLAw88ILL7iMa9KkiRk0aFC+67MLvtN2ldmzZ482b96s++67T5Lk7u6uXr16ad68eYVazr333qu77rpLEydO1Msvv6waNWoUuU1Hjx7VI488oho1asjpdMrpdColJSXXdzAaN25c5HXYQUH3ff369a2fK1SoIOnMPpKk1NRUjR49WnXq1FGZMmXk5+en3bt3F/j7Kn379lV8fLxq1qypoUOHasWKFRec52LXeTndfffdOnLkiD799FN16tRJX3/9tRo1aqT58+cXajmRkZHWz2XLllXNmjW1a9cuSVJcXJzmz58vPz8/69WpUydlZ2dr//791nzn/r6WL19eHTp00KJFiyRJ+/fv14YNG/TAAw/k2YZ7771Xp0+fVtWqVTVgwAAtXbrUuqd/165dcnd3V9OmTa36oKAgl3ZKZ75fevbv05XKGCNJ5/2e7NlGjRql+Ph4l9fZ++lC6ynIOuzuQueaf//734qJiVHDhg01evRorV+/3pq3MOeIopxP4uLi9Oyzz7r8/QwYMEAJCQkunW+c/Xub02FMznkwLz/99JP++ecfdejQwWXZCxYs0K+//nrBdpWEc3/XNm/erPj4eNWtW1dpaWmKi4tTSkqKgoKCXLZp//79LttUqVIllS9f3hou6HyVK1eWv7+/NVyhQoV893HOsr/66iuX5daqVUuSbLefly1bJj8/P5UuXVqRkZFq1aqVXnvtNUlF22fDhw/XQw89pPbt2+vFF1/Md3t37drl8j4iub6v/Pnnnzp06JD69+/vsr7nn38+13Lz+0yQl61bt8oYoxo1argse+3atbY7RgV1oXPz2e+3hdm3Zzt58qSOHDmiFi1auIxv0aKFy/vqueuzE/eSbgCK19y5c5WZmamKFSta44wx8vDwUFJSkkqVKmV9QMqR15cs//77b8XFxcnNzU0///zzRbWpb9+++vPPPzV9+nRVqlRJXl5eioyMzNV5g6+v70Wtp6RdaN/n8PDwsH7OOUnldCAxatQoffnll5oyZYqqVasmb29v3XPPPQXu6KJRo0bav3+/vvjiC61atUo9e/ZU+/bt9X//93/nnedi13m5lS5dWh06dFCHDh309NNP66GHHtK4ceP07bffSpLL73dhvkB89rEYOHCghg4dmqvm+uuvt37O6/f1gQce0GOPPabXXntNixcvVt26ddWgQYM8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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA20AAAIiCAYAAABbiyDHAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAewhJREFUeJzt3Xl0FFXe//FPyL52NpIQCBAhssgqKDuoKKAsOiIqYBTx5/gMIiKgiDMqbiDIOD7CoDgquMPMg7gNIqgIsokiiCgiKEoQAgRCJyFLZ6nfH9htOunudEKWSvJ+ncM5pOp21a26Vbfut27VLR/DMAwBAAAAAEypSV1nAAAAAADgHkEbAAAAAJgYQRsAAAAAmBhBGwAAAACYGEEbAAAAAJgYQRsAAAAAmBhBGwAAAACYGEEbAAAAAJgYQRsAAAAAmBhBGwAAHjz44INq2rSp9u/fX9dZAQA0UgRtABqMZcuWycfHx/HPz89PzZo104033ljlBvdnn30mHx8fffbZZ9Wb2VL27dun8847Ty1bttSKFSu0fPlyXXbZZTW2vuqyePFiLVu2rFbXmZaWpkmTJun8889XcHCwoqOj1blzZ91+++1KS0ur9PIqKt81a9bomWee0X//+1+lpKR4vVz7sfjLL79UOk/Vqew54e5f69at6zSftcXHx0ezZ8+utuWdOXNG8+bNU9euXRUREaHw8HC1adNG119/vTZs2FBt66mM2qizANQ+v7rOAABUt6VLl6p9+/bKz8/X5s2b9cQTT2j9+vX64YcfFBUVVdfZK2fZsmXq2bOnhg4dqgcffFAnTpzQK6+8UtfZqtDixYsVGxurCRMm1Mr6Dh8+rAsvvFCRkZGaPn262rVrJ6vVqu+//17//ve/9fPPPyspKana1peWlqYJEyZoxYoVuvjiiyv12+HDh2vr1q1q1qxZteWnKuz5KK1Pnz667rrrNH36dMe0wMDA2s5avVdcXKwhQ4bo22+/1b333us4Rvbv36/3339fn3/+uQYNGlTr+brwwgu1detWdezYsdbXDaDmELQBaHA6deqknj17SpIuueQSFRcX6+GHH9Y777yjW2+9tY5zV97cuXMd/7/tttvqMCc1p7Cw0NH7WVX/+te/lJGRoe3btys5Odkx/ZprrtEDDzygkpKS6siqQ1JSktLT0yv1m7y8PAUFBalp06Zq2rRpteanKtzlIz4+Xr17966DHDUcGzdu1JYtW/Tyyy871StDhw7V5MmTq+14LC4uVlFRkdeBdUREBGULNEA8HgmgwbMHcMeOHXOa/tVXX2nUqFGKjo5WUFCQunfvrn//+98VLu+rr77SjTfeqNatWys4OFitW7fW2LFj9euvv5ZL+9tvv+nPf/6zkpKSFBAQoMTERF133XWOvOTn52v69Onq1q2bLBaLoqOj1adPH7377rvllpWfn69Zs2YpOTlZAQEBat68ue68806dPn3aq/3gzfbaH6dbv369/vKXvyg2NlYxMTG69tprdeTIEUe61q1b67vvvtOGDRvKPWJnfzzrtdde0/Tp09W8eXMFBgbqwIEDkqSPP/5YgwcPVkREhEJCQtSvXz998sknFeb/5MmTatKkieLi4lzOb9Lkj0taZcrI1X7y5rf2fbV27VpNnDhRTZs2VUhIiAoKCtw+Hvnyyy+ra9euCgoKUnR0tP70pz9p7969FeZJktLT03XHHXeoRYsWCggIUHJysh555BEVFRV59XtP9u/fr3HjxikuLk6BgYHq0KGD/vnPfzqlsZfrm2++qZkzZ6pZs2YKCwvTyJEjdezYMWVnZ+vPf/6zYmNjFRsbq1tvvVU5OTlOy/Dx8dHkyZO1ZMkSnX/++QoMDFTHjh21fPnycnnas2ePrr76akVFRSkoKEjdunXzugc6KytLt99+u2JiYhQWFqZhw4bpxx9/rPK2u3Ly5ElJctubWvp4lLwrv19++UU+Pj6aP3++Hn/8cSUnJyswMFD//ve/FRAQoAcffLDcen744Qf5+Pjo2WefleT+8cgvvvhCI0eOVExMjIKCgtSmTRtNnTrVKc2mTZs0ePBghYeHKyQkRH379tV///vfCvcFgJpHTxuABu/gwYOSpPPPP98xbf369Ro2bJh69eql559/XhaLRcuXL9cNN9yg3Nxcj4/8/fLLL2rXrp1uvPFGRUdH6+jRo3ruued00UUX6fvvv1dsbKykswHbRRddpMLCQj3wwAPq0qWLTp48qY8++kiZmZmKj49XQUGBTp06pRkzZqh58+ay2Wz6+OOPde2112rp0qW6+eabJUmGYeiaa67RJ598olmzZmnAgAHavXu3Hn74YW3dulVbt271eCe+stv7//7f/9Pw4cP15ptvKi0tTffee69uuukmffrpp5KkVatW6brrrpPFYtHixYsllX/EbtasWerTp4+ef/55R7D1+uuv6+abb9bVV1+tV155Rf7+/lqyZImGDh2qjz76SIMHD3a7DX369NE///lPXXvttZo2bZr69OmjiIiIcyojV37++We1adNGY8aMUdOmTXX06FEtXrzY7W8nTpyo4cOH67XXXtOZM2fk7+/vcrlz587VAw88oLFjx2ru3Lk6efKkZs+erT59+ujLL7/0+M5cenq6Lr74YjVp0kQPPfSQ2rRpo61bt+rxxx/XL7/8oqVLl7r9bUW+//579e3bVy1bttTf//53JSQk6KOPPtKUKVOUkZGhhx9+2Cn9Aw88oEsvvVTLli3TL7/8ohkzZmjs2LHy8/NT165d9dZbb2nnzp164IEHFB4e7ggm7N577z2tX79ejz76qEJDQ7V48WLH76+77jpJZ9/z7Nu3r+Li4vTss88qJiZGr7/+uiZMmKBjx47pvvvuc7s99nNly5Yteuihh3TRRRdp8+bNuvLKK89520vr2bOn/P39dffdd+uhhx7SZZdd5jaAq2z5Pfvsszr//PO1YMECRUREKCUlRSNGjNArr7yiRx55xCkgXLp0qQICAjR+/Hi3ef3oo480cuRIdejQQU8//bRatmypX375RWvXrnWk2bBhg6644gp16dJFL730kgIDA7V48WKNHDlSb731lm644Qa3ywdQCwwAaCCWLl1qSDK2bdtmFBYWGtnZ2caaNWuMhIQEY+DAgUZhYaEjbfv27Y3u3bs7TTMMwxgxYoTRrFkzo7i42DAMw1i/fr0hyVi/fr3b9RYVFRk5OTlGaGio8b//+7+O6RMnTjT8/f2N77//3uttKCoqMgoLC43bbrvN6N69u2P6mjVrDEnG/PnzndKvWLHCkGS88MILHpfr7fba9+GkSZOc0s2fP9+QZBw9etQx7YILLjAGDRpUbl32fTZw4ECn6WfOnDGio6ONkSNHOk0vLi42unbtalx88cUet6GkpMS44447jCZNmhiSDB8fH6NDhw7GPffcYxw8eNDjb92VkTflaxiGkZeXZ4SEhDj91r6vbr755nLp7fPs+crMzDSCg4ONq666yindoUOHjMDAQGPcuHEe13/HHXcYYWFhxq+//uo0fcGCBYYk47vvvvP4+9IkGXfeeafj76FDhxotWrQwrFarU7rJkycbQUFBxqlTpwzD+GNflS2/qVOnGpKMKVOmOE2/5pprjOjo6HLrDg4ONtLT0x3TioqKjPbt2xtt27Z1TLvxxhuNwMBA49ChQ06/v/LKK42QkBDj9OnTbrfvww8/NCQ5lZVhGMYTTzxhSDIefvjhSm+7Oy+99JIRFhZmSDIkGc2aNTNuvvlmY+PGjU7pvC2/gwcPGpKMNm3aGDabzSnte++9Z0gy1q5d65hWVFRkJCYmGqNHj3ZMc3VMt2nTxmjTpo2Rl5fndlt69+5txMXFGdnZ2U7L79Spk9GiRQujpKTE474AULN4PBJAg9O7d2/5+/srPDxcw4YNU1RUlN59913H+1QHDhzQDz/84LgzXVRU5Ph31VVX6ejRo9q3b5/b5efk5GjmzJlq27at/Pz85Ofnp7CwMJ05c8bpUbcPP/xQl156qTp06OAxv//5z3/Ur18/hYWFyc/PT/7+/nrppZeclmXv4SrbIzZmzBiFhoZ6fLywKts7atQop7+7dOkiSV49Xmg3evRop7+3bNmiU6dO6ZZbbnHKQ0lJiYYNG6Yvv/xSZ86ccbs8Hx8fPf/88/r555+1ePFi3XrrrSosLNQ//vEPXXDBBU6j9XlbRq7k5eXpkUceUdeuXRUZGang4GBFRkYqNzfX5W/LbqcrW7duVV5eXrnyS0pK0mWXXVbh46EffPCBLr30UiUmJjrtO3vvUVVHKszPz9cnn3yiP/3pTwoJCSl3bOTn52vbtm1OvxkxYoTT3/bje/jw4eWmnzp1qtwjkoMHD1Z8fLzjb19fX91www06cOCADh8+LOns8T548OByA8tMmDBBubm55QZXKW39+vWSVK7nady4cee87WVNnDhRhw8f1ptvvqkpU6YoKSlJr7/+ugYNGqSnnnrKka6y5Tdq1KhyPbZXXnmlEhISnHrlPvroIx05ckQTJ050m8cff/xRP/30k2677TYFBQW5THPmzBl98cUXuu666xQWFuaY7uvrq9TUVB0+fNhjnQig5vF4JIAG59VXX1WHDh2UnZ2tFStWaMmSJRo7dqw+/PBDSX+82zZjxgzNmDHD5TIyMjLcLn/cuHH65JNP9OCDD+qiiy5SRESEfHx8dNVVVykvL8+R7sSJE2rRooXHvL799tu6/vrrNWbMGN17771KSEiQn5+fnnvuOb388suOdCdPnpSfn1+5QSV8fHyUkJDgeL/Glapsb0xMjNPf9kcfS29fRco+KmbPh/0ROFdOnTql0NBQj8tt1aqV/vKXvzj+/ve//62xY8fq3nvv1fbt2yV5X0au3HTTTVq7dq2eeOIJXXzxxbJYLPLx8dGgQYNc/tabESI9vf+UmJiodevWefz9sWPH9P7777t99NLT8VpRvoqKirRw4UItXLjQq2VHR0c7/R0QEOBxen5+vlMgkJCQUG4d9mknT55UixYtdPLkSbf7yp7O0zb5+fmVO4bLrrcq2+6KxWLR2LFjNXbsWEnSd999p8svv1x//etfdfvttysyMrLS5edq2/38/JSamqqFCxfq9OnTioyM1LJly9SsWTMNHTrUbf5OnDghSR7roszMTBmGUeV9DqDmEbQBaHA6dOjgGHzk0ksvVXFxsV588UX93//9n6677jrHO0mzZs3Stdde63IZ7dq1czndarXqgw8+0MMPP6z777/fMd3+blppTZs2dfQcuPP6668rOTlZK1askI+Pj9PySouJiVFRUZFOnDjhFLgZhqH09HRddNFFbtdxLtt7LkpvT+l8LFy40O3odqV7YLx1/fXXa+7cudqzZ4+kypVRWVarVatWrdIjjzyiKVOmOKbn5+e7bcCX3U5X7AHE0aNHy807cuSIx3fspLP7rkuXLnriiSdczrc3rCsrKirK0Zty5513ukxTeqTO6uBqRE77NPt+iomJcbuvJHncX/Zz5eTJk06BW9n11tS2X3DBBbrxxhv1zDPP6Mcff9TFF19c6fJzd0zdeuuteuqppxzvo7733nuaOnWqfH193ebHXl94qouioqLUpEmTKu9zADWPoA1Agzd//nytXLlSDz30kK699lq1a9dOKSkp+uabbzRnzpxKLcvHx0eGYZQbdOPFF19UcXGx07Qrr7xSr732mvbt2+c2KPLx8VFAQIBTIy09Pb3c6JGDBw/W/Pnz9frrr+uee+5xTF+5cqXOnDnjcQCPc9leTwIDAyvV89avXz9FRkbq+++/1+TJkyu9vqNHj7rsCcjJyVFaWpqj4VuZMirL/tuyjeAXXnjhnIZw79Onj4KDg/X6669rzJgxjumHDx/Wp59+6rH3UTr7SOLq1avVpk2bav3WYEhIiC699FLt3LlTXbp0cfSO1aRPPvlEx44dcwToxcXFWrFihdq0aePoDRo8eLBWrVqlI0eOOAU0r776qkJCQjwOaX/ppZdq/vz5euONN5wC7zfffNMp3blu+8mTJxUeHu7ydz/88IOkP4Kx6iq/Dh06qFevXlq6dKmKi4tVUFBQ4WdMzj//fLVp00Yvv/yypk2b5nLAotDQUPXq1Utvv/22FixYoODgYElSSUmJXn/9dbVo0cJpICcAtY+gDUCDFxUVpVmzZum+++7Tm2++qZtuuklLlizRlVdeqaFDh2rChAlq3ry5Tp06pb179+rrr7/Wf/7zH5fLioiI0MCBA/XUU08pNjZWrVu31oYNG/TSSy8pMjLSKe2jjz6qDz/8UAMHDtQDDzygzp076/Tp01qzZo2mTZum9u3ba8SIEXr77bc1adIkXXfddUpLS9Njjz2mZs2aaf/+/Y5lXXHFFRo6dKhmzpyprKws9evXzzF6ZPfu3ZWamupxH1R1ez3p3Lmzli9frhUrVui8885TUFCQOnfu7DZ9WFiYFi5cqFtuuUWnTp3Sddddp7i4OJ04cULffPONTpw4oeeee87t75944glt3rxZN9xwg7p166bg4GAdPHhQixYt0smTJx3vEFWmjMqKiIjQgAEDtGDBAjVt2lTJyclav369li5dWuFvPYmMjNSDDz6oBx54QDfffLPGjh2rkydP6pFHHlFQUJDHUQqls8fSunXr1LdvX02ZMkXt2rVTfn6+fvnlF61evVrPP/98hY/iuvO///u/6t+/vwYMGKC//OUvat26tbKzs3XgwAG9//77jvcpq0tsbKwuu+wyPfjgg47RI3/44QenYf8ffvhhx3tgDz30kKKjo/XGG2/ov//9r+bPny+LxeJ2+UOGDNHAgQN133336cyZM+rZs6c2b96s1157rVq3ff369br77rs1fvx49e3bVzExMTp+/LjeeustrVmzRjfffLOjTKqz/CZOnKg77rhDR44cUd++fb3qJf/nP/+pkSNHqnfv3rrnnnvUsmVLHTp0SB999JHeeOMNSWdHN73iiit06aWXasaMGQoICNDixYu1Z88evfXWW171KAOoQXU6DAoAVCP7iH1ffvlluXl5eXlGy5YtjZSUFKOoqMgwDMP45ptvjOuvv96Ii4sz/P39jYSEBOOyyy4znn/+ecfvXI3EdvjwYWP06NFGVFSUER4ebgwbNszYs2eP0apVK+OWW25xWm9aWpoxceJEIyEhwZBkREREGNdff71x7NgxR5onn3zSaN26tREYGGh06NDB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17hx43THHXdo1qxZ+uqrryRJkydPdvrNgQMH9O9//1vvv/++1qxZo127dunOO+90zP/f//1f/f3vf9eCBQu0e/duDR06VKNGjdL+/fvd5vfee+/V+vXrtWrVKq1du1afffaZduzY4ZTm1ltv1ebNm7V8+XLt3r1bY8aM0bBhw9wuNyEhQUVFRVq1apUMw3CZ5ujRoxo0aJC6deumr776SmvWrNGxY8d0/fXXO6V75ZVX5Ofnp82bN2vJkiUaP3683nvvPeXk5Djt8zNnzmj06NEu13XzzTdr+fLlevbZZ7V37149//zzCgsLkyT99ttvuuqqq3TRRRfpm2++0XPPPaeXXnpJjz/+uNt9BgCogAEAgIksXbrUsFgsjr8HDBhgzJkzxynNa6+9ZjRr1szxtyTjb3/7m+PvrVu3GpKMl156yTHtrbfeMoKCghx/P/zww4avr6+RlpbmmPbhhx8aTZo0MY4ePWoYhmEkJiYaTzzxhNO6L7roImPSpEku856dnW0EBAQYy5cvd0w7efKkERwcbNx9992GYRjGgQMHDB8fH+O3335z+u3gwYONWbNmuVyuYRjGAw88YPj5+RnR0dHGsGHDjPnz5xvp6emO+Q8++KAxZMgQp9+kpaUZkox9+/YZhmEYgwYNMrp16+aUxmazGbGxscarr77qmDZ27FhjzJgxjr8HDRrkyP++ffsMSca6devc5rNdu3ZGSUmJY9o///lPIywszCguLna7fQAA9+hpAwCY2o4dO/Too48qLCzM8e/222/X0aNHnd7n6tKli+P/8fHxkqTOnTs7TcvPz1dWVpZjWsuWLdWiRQvH33369FFJSYn27dunrKwsHTlyRP369XPKT79+/bR3716Xef3pp59ks9nUp08fx7To6Gi1a9fO8ffXX38twzB0/vnnO23Thg0bnB7fLOuJJ55Qenq6nn/+eXXs2FHPP/+82rdvr2+//daxn9avX++0zPbt2zvyZdezZ0+n5fr7+2vMmDF64403JJ19vPPdd9/V+PHjXeZj165d8vX11aBBg1zO37t3r/r06SMfHx+nfZaTk6PDhw+73T4AgHsMRAIAMLWSkhI98sgjuvbaa8vNCwoKcvzf39/f8X97wOBqWklJidt12dOUDjhK/1+SDMMoN630vIqUlJTI19dXO3bskK+vr9M8+yOG7sTExGjMmDEaM2aM5s6dq+7du2vBggV65ZVXVFJSopEjR2revHnlftesWTPH/0NDQ8vNHz9+vAYNGqTjx49r3bp1CgoK0pVXXukyDxUNCuNq/9j3i7v9BgDwjKANAGBqF154ofbt26e2bdtW+7IPHTqkI0eOKDExUZK0detWNWnSROeff74iIiKUmJioTZs2aeDAgY7fbNmyRRdffLHL5bVt21b+/v7atm2bY4CQzMxM/fjjj46eqe7du6u4uFjHjx/XgAEDqpz3gIAAtWnTRmfOnJF0dj+tXLlSrVu3lp9f5S7vffv2VVJSklasWKEPP/xQY8aMcTuqZOfOnVVSUqINGzbo8ssvLze/Y8eOWrlypVPwtmXLFoWHh6t58+aV3EoAgMRAJAAAk3vooYf06quvavbs2fruu++0d+9erVixQn/729/OedlBQUG65ZZb9M033+jzzz/XlClTdP311yshIUHS2UFF5s2bpxUrVmjfvn26//77tWvXLt19990ulxcWFqbbbrtN9957rz755BPt2bNHEyZMUJMmf1xuzz//fI0fP14333yz3n77bR08eFBffvml5s2bp9WrV7tc7gcffKCbbrpJH3zwgX788Uft27dPCxYs0OrVq3X11VdLku68806dOnVKY8eO1fbt2/Xzzz9r7dq1mjhxooqLiz3uBx8fH40bN07PP/+81q1bp5tuuslt2tatW+uWW27RxIkT9c477+jgwYP67LPP9O9//1uSNGnSJKWlpemuu+7SDz/8oHfffVcPP/ywpk2b5rQfAADeo6cNAGBqQ4cO1QcffKBHH31U8+fPl7+/v9q3b6//9//+3zkvu23btrr22mt11VVX6dSpU7rqqqu0ePFix/wpU6YoKytL06dP1/Hjx9WxY0e99957SklJcbvMp556Sjk5ORo1apTCw8M1ffp0Wa1WpzRLly7V448/runTp+u3335TTEyM+vTpo6uuusrlMjt27KiQkBBNnz5daWlpjmH2X3zxRaWmpkqSEhMTtXnzZs2cOVNDhw5VQUGBWrVqpWHDhnkVLI0fP15z5sxRq1atyr3HV9Zzzz2nBx54QJMmTdLRo0fVtm1bPfDAA5Kk5s2ba/Xq1br33nvVtWtXRUdH67bbbquWIBsAGisfw5sH8AEAaGBmz56td955R7t27arrrNRrd9xxh66//noNHjy4rrMCAA0WzykAAIBKs1qt+umnnxQQEKD33nuvrrMDAA0aj0cCAIBK++2339S7d28FBgbq9ddfr+vsAECDxuORAAAAAGBiPB4JAAAAACZG0AYAAAAAJkbQBgAAAAAmRtAGAAAAACZG0AYAAAAAJkbQBgAAAAAmRtAGAAAAACZG0AYAAAAAJvb/AZgirTKkeSq+AAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Cria um gráfico de barras para mostrar a média salarial por cargo:\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(x=df['CARGO'], y=df['SALÁRIO'])\n",
    "plt.title('Média Salarial por Cargo')\n",
    "plt.xlabel('Cargo')\n",
    "plt.ylabel('Salário')\n",
    "plt.show()\n",
    "\n",
    "# Cria uma nova coluna com o tempo de serviço:\n",
    "\n",
    "from datetime import date\n",
    "df['DATA-ADMISSÃO'] = pd.to_datetime(df['DATA-ADMISSÃO'])\n",
    "df['TEMPO DE SERVIÇO'] = (date.today() - df['DATA-ADMISSÃO'].dt.date).apply(lambda x: x.days)\n",
    "\n",
    "# Cria um scatter plot para mostrar a relação entre salário e tempo de serviço:\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.scatterplot(x=df['TEMPO DE SERVIÇO'], y=df['SALÁRIO'])\n",
    "plt.title('Relação entre Salário e Tempo de Serviço')\n",
    "plt.xlabel('Tempo de Serviço')\n",
    "plt.ylabel('Salário')\n",
    "plt.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b6c1a9f-a89b-4c75-8b89-783a34900f24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['NOME', 'ID-REGISTRO', 'DATA-ADMISSÃO', 'CARGO', 'SALÁRIO',\n",
      "       'CIDADE-ATUAÇÃO', 'LOJA'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "# Verifica se a coluna existe no DataFrame:\n",
    "\n",
    "print(df.columns)\n",
    "\n",
    "# Renomeia a coluna para o nome correto:\n",
    "\n",
    "df = df.rename(columns={'TEMPO_DE_SERVICO': 'TEMPO DE SERVIÇO'})\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9cdcaac4-e067-4595-8e12-9b876786db90",
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
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

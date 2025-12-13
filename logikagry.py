{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNLGjhly74m3/p48CExgXjt",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/katarzynali/kurs-git-1/blob/main/logikagry.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def utworz_nowe_id(zadania:str):\n",
        "    if not zadania:               #funkcja zwraca ID dla nowego zdania, który\n",
        "                                  #jest równy 1, jesli lista zadań jest pusta\n",
        "        ID = 1                    #lub jest następnym kolejnym numerem\n",
        "\n",
        "    else: ID = len(zadania)+1\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "dULKMse79VW4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def dodaj_zadanie(zadania:str, nazwa:str, osoba:str):\n",
        "    zad_id = utworz_nowe_id(zadania)\n",
        "    zadania.append({                       #funkcja automatycznie nadaje nowe ID\n",
        "        \"ID\": zad_id,                      #i dodaje nowe zadanie\n",
        "        \"nazwa\" : nazwa,\n",
        "        \"osoba\": osoba,\n",
        "        \"status\": 0\n",
        "})\n"
      ],
      "metadata": {
        "id": "sgLpbTsCGlik"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def usun_zadanie(zadania, zad_id):\n",
        "\n",
        "     for i, zad in enumerate(zadania):     #funkcja przechodzi przez listę zadań\n",
        "        if zad[\"zadID\"] == zad_id:         #szuka zadania z podanym indyfikatorem (zad_id)\n",
        "            del zadania[i]                 #usuwa je z listy\n",
        "\n"
      ],
      "metadata": {
        "id": "c-uLJKe7MHpw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def zmien_status_zadania(zadania, zad_id, nowy_status):\n",
        "        if not 0 <= nowy_status <= 1:          #funkcja sprawdza czy nowy status\n",
        "            return                             #jest poprawny, następnie przeglada\n",
        "                                               #listę zadań, aby zaktualizować status\n",
        "        for zadanie in zadania:\n",
        "            if zadanie['ID'] == zad_id:\n",
        "                zadanie['status'] = nowy_status\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "1JD3WfgNXe0N"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
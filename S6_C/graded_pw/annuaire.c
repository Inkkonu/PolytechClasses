#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAILLE_ANNUAIRE 128
#define TAILLE_NOMS 20

struct SEtudiant{
  char* nom;
  char* prenom;
  int age;
  int anneeInscription;
};

typedef struct SEtudiant SEtudiant;

struct SAnnuaire{
  SEtudiant** etudiants;
  int nbEtudiants;
  int index;
};

typedef struct SAnnuaire SAnnuaire;

SAnnuaire* GenererAnnuaire(){
  SAnnuaire* annuaire = (SAnnuaire *) malloc(sizeof(SAnnuaire));
  annuaire->etudiants = (SEtudiant **) malloc(sizeof(SEtudiant) * TAILLE_ANNUAIRE);
  annuaire->index = 0;
  annuaire->nbEtudiants = 0;
  return annuaire;
}

void SupprimerAnnuaire(SAnnuaire* annuaire){
  free(annuaire->etudiants);
  free(annuaire);
}

void demanderNom(char* nom){
  printf("Entrez le nom : ");
  scanf("%s", nom);
}

void demanderPrenom(char* prenom){
  printf("Entrez le prénom : ");
  scanf("%s", prenom);
}

void demanderAge(int* age){
  printf("Entrez l'âge : ");
  scanf("%d", age);
}

void demanderAnneeInscription(int* annee){
  printf("Entrez l'année d'inscription : ");
  scanf("%d", annee);
}

SAnnuaire* SaisirAnnuaire(SAnnuaire* annuaire){
  char* nom = malloc(TAILLE_NOMS * sizeof(char));
  char* prenom = malloc(TAILLE_NOMS * sizeof(char));
  int age;
  int anneeInscription;
  demanderNom(nom);
  demanderPrenom(prenom);
  demanderAge(&age);
  demanderAnneeInscription(&anneeInscription);
  SEtudiant* etudiant = (SEtudiant *) malloc(sizeof(SEtudiant));
  etudiant->prenom = malloc(sizeof(char) * TAILLE_NOMS);
  etudiant->nom = malloc(sizeof(char) * TAILLE_NOMS);
  strcpy(etudiant->nom, nom);
  strcpy(etudiant->prenom, prenom);
  etudiant->age = age;
  etudiant->anneeInscription = anneeInscription;
  annuaire->etudiants[annuaire->nbEtudiants] = etudiant;
  annuaire->nbEtudiants++;
  int answer;
  printf("Ajouter un autre ? (1 oui, 2 non)\n");
  scanf("%d", &answer);
  if(answer == 1){
    SaisirAnnuaire(annuaire);
  }
  return annuaire;
}

void AfficherAnnuaire(SAnnuaire* annuaire){
  if(annuaire->nbEtudiants == 0){
    printf("Annuaire vide\n");
  }
  else{
    for(int i = 0 ; i < annuaire->nbEtudiants ; i++){
      printf("Étudiant %d :\n", i);
      printf("   Nom : %s\n", annuaire->etudiants[i]->nom);
      printf("   Prénom : %s\n", annuaire->etudiants[i]->prenom);
      printf("   Age : %i ans\n", annuaire->etudiants[i]->age);
      printf("   Année d'inscription : %i\n", annuaire->etudiants[i]->anneeInscription);
    }
  }
}

int EnregistrerAnnuaire(SAnnuaire* annuaire, char* filename){
  FILE *pFile;
  if(pFile = fopen(filename, "w")){
    for(int i = 0 ; i < annuaire->nbEtudiants ; i++){
      fprintf(pFile, "%s,", annuaire->etudiants[i]->nom);
      fprintf(pFile, "%s,", annuaire->etudiants[i]->prenom);
      fprintf(pFile, "%i,", annuaire->etudiants[i]->age);
      fprintf(pFile, "%i\n", annuaire->etudiants[i]->anneeInscription);
    }
    fclose(pFile);
  }
  else{
    return -1;
  }
}

SAnnuaire* LireAnnuaire(char* filename){
  FILE *pFile;
  char c;
  int i = 0;
  char* nom = malloc(TAILLE_NOMS * sizeof(char));
  int index = 0;
  char* prenom = malloc(TAILLE_NOMS * sizeof(char));
  int age = 0;
  int anneeInscription = 0;
  SEtudiant* etudiant = (SEtudiant *) malloc(sizeof(SEtudiant));
  SAnnuaire* annuaire = GenererAnnuaire();
  if(pFile = fopen(filename, "r")){
    while(!feof(pFile)){
      c = fgetc(pFile);
      
      if(c == ','){
        switch(i){
          case 0:
            strcpy(etudiant->nom, nom);
            break;
          case 1:
            strcpy(etudiant->prenom, prenom);
            break;
          case 2:
            etudiant->age = age;
            break;
          //Pour l'année d'inscription, c'est géré quand \n est rencontré 
        }
        index = 0;
        i++;
      }
      else if(c == '\n'){
        etudiant->anneeInscription = anneeInscription;
 
        annuaire->etudiants[i] = etudiant;
        annuaire->nbEtudiants++;
        
        i = 0;
        etudiant = (SEtudiant *) malloc(sizeof(SEtudiant));
        nom = malloc(TAILLE_NOMS * sizeof(char));
        index = 0;
        prenom = malloc(TAILLE_NOMS * sizeof(char));
        age = 0;
        anneeInscription = 0;
      }
      else{
        switch(i){
          case 0:
            nom[index] = c;
            break;
          case 1:
            prenom[index] = c;
            break;
          case 2:
            age = age * 10 + c - 48; //Car le code ASCII de 0 est 48
            break;
          case 3:
            anneeInscription = anneeInscription * 10 + c - 48;
        }
        index++;
      }
    }
    fclose(pFile);
    return annuaire;
  }
  else{
    return NULL;
  }
}

int main(){
  SAnnuaire* annuaire = GenererAnnuaire();
  annuaire = SaisirAnnuaire(annuaire);
  AfficherAnnuaire(annuaire);
  EnregistrerAnnuaire(annuaire, "etudiants.txt");
  annuaire = LireAnnuaire("etudiants.txt");
  AfficherAnnuaire(annuaire);
  return 0;
}

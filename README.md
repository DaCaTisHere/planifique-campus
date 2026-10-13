# Planifique Campus

Vue 3D gamifiée de Planifique Groupe, destinée à la direction : plateau
isométrique façon maquette d'architecte, 14 équipes, 98 collaborateurs avec
leur photo, parcours clients animés et fiches CRM.

> Prototype : l'organisation, les rôles et les photos viennent de l'annuaire
> public du site Planifique. Statuts, rendez-vous, charge et clients sont
> **simulés**. Le branchement Salesforce est décrit dans `docs/SPEC.md`.

## Organisation représentée

| Ensemble | Où sur le plateau | Équipes |
| --- | --- | --- |
| Direction | Estrade centrale avec mur de données temps réel | 5 associés + assistante |
| Pôle Retraite | Aile nord-ouest, deux équipes reliées par une verrière | Planification Retraite → Démarches Retraite |
| Pôle Gestion Privée | Aile nord-est | Gestion Privée, Ingénierie & Family Office, Immobilier |
| Pôle Fiscalité & Audit | Aile sud-ouest | Planifique Audit |
| Relation client | Entrée ouest et coin sud-est | Accueil, Suivi Clients |
| Fonctions support | Aile sud | IT & Data, RH, Administration & Opérations, Marketing & Growth |
| Business Development | Pavillon externe, hors du bâtiment | Service externe d'appels sortants, prend les RDV pour tous les pôles |

## Ce que fait chaque service sur la maquette

| Service | Reconnaissable à | Activité animée |
| --- | --- | --- |
| Planification Retraite | Deux salons de RDV sur place | RDV sur place avec les clients, et RDV à domicile : le conseiller prend une voiture au parking et va chez le client |
| Démarches Retraite | Armoires et piles de dossiers | Demandes envoyées aux caisses de pension, avoirs LPP récupérés en retour |
| Suivi Clients | Casques, écran du nombre d'appels | Appels de suivi vers les maisons des clients, relances à 90 jours |
| Immobilier | Maquettes de maisons, tableau des biens | Visites en voiture des maisons « À vendre », ventes qui passent à « Vendu » |
| Gestion Privée | Écran des marchés, fauteuils | RDV patrimoniaux, mandats signés |
| Ingénierie & Family Office | Tableau blanc | Études patrimoniales |
| Fiscalité & Audit | Liasses et calculatrices | Audits et déclarations |
| Informatique & Data | Baies serveurs aux LEDs, kanban | Tickets traités |
| Marketing & Growth | Affiches des livres blancs | Leads envoyés au Business Development |
| Business Development | Pavillon externe, casques, écran des leads | Appels, RDV pris pour les pôles |

Un clic sur une équipe zoome dessus, l'entoure d'un contour lumineux et ouvre une carte d'activité en direct. Le panneau affiche les chiffres du jour (compteurs animés), l'historique sur 7 jours et le journal d'activité.

## Modes et effets

- **Organisation** : panneaux de pôles de loin, équipes de près ; clic sur un pôle, une équipe ou une personne.
- **Organigramme** : chaque associé référent relié à son pôle, chaque pôle à ses équipes, responsables cerclés.
- **Parcours client** : chemin animé au sol, de l'appel du Business Development jusqu'au Suivi.
- **Charge** : colonnes lumineuses par équipe.
- **Jour et nuit** : éclairage à l'heure de Genève, ou Matin / Midi / Soir / Nuit ; lampes de bureau, lampadaires et halos la nuit.
- Intro animée, arcs d'appel du pavillon vers les pôles, ondes à chaque étape, +XP, confettis en fin de parcours, recherche, focus sur une équipe.

## Contenu

| Chemin | Rôle |
| --- | --- |
| `campus/index.html` | Page autonome (Three.js r128 via CDN, photos embarquées) |
| `campus/index.template.html` | Même page sans les photos (`/*PHOTOS*/` à remplacer) |
| `tools/photos/build_photos.py` | Régénère les photos et `index.html` à partir du template |
| `tools/photos/annuaire.txt` | Correspondance nom → fichier photo de l'annuaire |
| `docs/SPEC.md` | Lien vers la spécification Salesforce |

## Lancer

Ouvrir `campus/index.html` dans un navigateur, ou `npx serve campus`.

## Prochaines étapes (voir la spécification)

1. Remplacer `ZONES`, `PEOPLE` et `JOURNEYS` par `GET /api/campus/snapshot`.
2. Brancher le flux d'événements `GET /api/campus/events` (SSE).
3. Remplacer les photos embarquées par `GET /api/photos/{userId}.jpg`.

## Données personnelles

Les noms, rôles et photos proviennent de l'annuaire public du site Planifique.
Ce dépôt sert à transmettre le code et le design du prototype ; le projet de
production, branché sur Salesforce, sera développé dans un dépôt privé. Tout
collaborateur peut demander le retrait de sa photo (nLPD / RGPD).

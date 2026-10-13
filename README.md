# Planifique Campus

Vue 3D gamifiée de Planifique Groupe, destinée à la direction : plateau
isométrique façon maquette d'architecte, 14 équipes, 98 collaborateurs avec
leur photo, parcours clients animés et fiches CRM.

> Prototype : l'organisation, les rôles et les photos viennent de l'annuaire
> public du site Planifique. Statuts, rendez-vous, charge et clients sont
> **simulés**. Le branchement Salesforce est décrit dans `docs/SPEC.md`.

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

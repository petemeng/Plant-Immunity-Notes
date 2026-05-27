# Tomato scRNA Marker Sources

This note accompanies `gene_sets/tomato_scRNA_marker_sources.tsv`. The table is designed for tomato single-cell or single-nucleus annotation and module scoring, especially root samples with Mock, *Meloidogyne* and bacterial treatments.

## Evidence Levels

| Level | Meaning | Recommended use |
|---|---|---|
| A | Tomato evidence plus experimental validation, such as promoter:GUS or strong functional support | High-priority module genes |
| B | Tomato scRNA/snRNA marker panel or tomato single-cell cluster-specific marker | Use for annotation with multiple genes per cell type |
| C | Tomato single-cell paper marker, but mainly symbol-level or Arabidopsis-homolog assisted | Use only after mapping to exact tomato `Solyc` IDs |
| D | Functional or infection-response candidate, not a clean cell identity marker | Use for response scoring and candidate ranking |

## Main Sources

| Source | Context | What was used |
|---|---|---|
| [A suberized exodermis is required for tomato drought tolerance](https://www.nature.com/articles/s41477-023-01567-x) | 7-day M82 tomato root scRNA atlas | Root cell-type markers for trichoblast, atrichoblast, exodermis, cortex, endodermis, pericycle, phloem/procambium, xylem, root cap/columella/QC and meristematic zone |
| [Single-nucleus transcriptomic analysis uncovers regulatory mechanisms of apical hook development and shade avoidance syndrome in tomato](https://academic.oup.com/hr/advance-article/doi/10.1093/hr/uhag044/8489356) | Tomato apical hook/hypocotyl snRNA atlas | Epidermal, cortex, exodermis-like, endodermis-like, phloem/cambium and xylem markers |
| [Dissecting the cell-type-specific response of tomato leaves to ToBRFV infection by single-cell RNA-seq](https://pmc.ncbi.nlm.nih.gov/articles/PMC13110166/) | Tomato leaf scRNA atlas under ToBRFV infection | Leaf marker symbols for epidermal, mesophyll, xylem, phloem, meristem/proliferating, guard and trichome cells |
| [Single-nucleus RNA-sequencing reveals the cellular programs driving nematode-induced giant cell formation in tomato](https://academic.oup.com/hr/article/doi/10.1093/hr/uhaf223/8239697) | Tomato root galls induced by *Meloidogyne incognita* | Known giant-cell markers, promoter:GUS validated giant-cell markers, C16 cluster-specific markers and VIGS functional candidates |

## Practical Annotation Notes

- Use module scores rather than single markers. A minimum of 3 markers per cell type/state is safer.
- Cell-cycle genes such as `CycA`, `CycB`, `CycD`, tubulin and MAP65 indicate proliferating or endoreduplicating states. In infected roots, they should not be used alone to call giant cells.
- For nematode-infected roots, call a cluster `giant cell-like` only when it is enriched in gall samples and co-expresses giant-cell markers such as `CCS52B`, `cdc2b`, `CycA/CycB`, `MAP65-3`, `Formin`, `AUX1/PIN4`, `ENG/PLL`, plus tomato-validated markers such as `Solyc11g069470`, `Solyc11g005090`, `Solyc03g115150` or `Solyc03g093260`.
- Leaf markers in this table are symbol-level because the paper uses Arabidopsis-homolog assisted annotation. Map them to exact tomato `Solyc` IDs before scoring.
- Functional candidates from VIGS are useful for ranking susceptibility genes but should not be treated as clean cell identity markers.

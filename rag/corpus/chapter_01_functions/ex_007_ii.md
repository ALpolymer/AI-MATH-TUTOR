---
content_type: solved_exercise
chapter: "1.2"
topic: synartiseis
concepts:
  - pedio_orismoy
  - synthesi_synartisewn
  - pedio_orismou_synthesis
  - periorismos_rizas
  - trigonometriki_synartisi
core_techniques:
  - idiotites_rizwn
  - trigwnometriki_tautotita
difficulty: medium
source_type: textbook
book_page: 28
book_exercise_number: "10"
sub_question: ii
exam_year: null
exam_theme: null
external_source_name: null
---

# ΕΚΦΩΝΗΣΗ

Να προσδιορίσετε τη συνάρτηση $g \circ f$, αν

i) $f(x) = x^2$ και $g(x) = \sqrt{x}$,
ii) $f(x) = \sin x$ και $g(x) = \sqrt{1-x^2}$
iii) $f(x) = \dfrac{\pi}{4}$ και $g(x) = \tan x$.

## Υποερώτημα ii

ii) $f(x) = \sin x$ και $g(x) = \sqrt{1-x^2}$

## Λύση

Η $f$ έχει πεδίο ορισμού το σύνολο $D_f = \mathbb{R}$, ενώ η $g$ το $D_g = [-1, 1]$.
Για να ορίζεται η παράσταση $g(f(x))$ πρέπει:
$$(x \in D_f \text{ και } f(x) \in D_g) \Leftrightarrow (x \in \mathbb{R} \text{ και } f(x) \in [-1, 1])$$
$$\Leftrightarrow \sin x \in [-1, 1] \Leftrightarrow x \in \mathbb{R}.$$

Επομένως, η $g \circ f$ ορίζεται για κάθε $x \in \mathbb{R}$ και έχει τύπο
$$(g \circ f)(x) = g(f(x)) = g(\sin x) = \sqrt{1-\sin^2 x} = \sqrt{\cos^2 x} = |\cos x|.$$

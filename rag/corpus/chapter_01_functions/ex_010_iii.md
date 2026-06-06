---
content_type: solved_exercise
chapter: "1.2"
topic: synartiseis
concepts:
  - aposynthesi_synartisewn
core_techniques:
  - trigwnometriki_tautotita
  - trigonometriki_synartisi
  - idiotites_rizwn
difficulty: medium
source_type: textbook
book_page: 30
book_exercise_number: "6"
subquestion: iii
exam_year: null
exam_theme: null
external_source_name: null
---

# ΕΚΦΩΝΗΣΗ

Να βρείτε συνάρτηση $f$ τέτοια, ώστε να ισχύει:

i) $(f \circ g)(x) = x^2 + 2x + 2$, για κάθε $x \in \mathbb{R}$, αν $g(x) = x + 1$
ii) $(f \circ g)(x) = \sqrt{1+x^2}$, για κάθε $x \in \mathbb{R}$, αν $g(x) = -x^2$
iii) $(g \circ f)(x) = |\cos x|$, για κάθε $x \in \mathbb{R}$, αν $g(x) = \sqrt{1-x^2}$

## Υποερώτημα iii

iii) $(g \circ f)(x) = |\cos x|$, για κάθε $x \in \mathbb{R}$, αν $g(x) = \sqrt{1-x^2}$

## Λύση

Έχουμε:

$$g(f(x)) = |\cos x|$$

Θέτουμε στην $g(x)$ όπου $x = f(x)$

άρα

$$ \sqrt{1-f^2(x)} = |\cos x| \Leftrightarrow 1-f^2(x) = \cos^2 x$$$

$$\Leftrightarrow f^2(x) = 1-\cos^2 x \Leftrightarrow f^2(x) = \sin^2 x $$

$$ \Leftrightarrow \sqrt{f^2(x)} = \sqrt{\sin^2 x} \Leftrightarrow |f(x)| = |\sin x|. $$

Μια τέτοια συνάρτηση είναι π.χ. η συνάρτηση
$f(x) = |\sin x|$,
ή η συνάρτηση
$f(x) = \sin x$
ή η συνάρτηση
$f(x) = -\sin x$ κ.τ.λ.

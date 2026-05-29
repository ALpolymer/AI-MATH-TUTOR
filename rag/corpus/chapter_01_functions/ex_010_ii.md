---
content_type: solved_exercise
chapter: "1.2"
topic: synartiseis
concepts:
  - aposynthesi_synartisewn
core_techniques:
  - voithitiki_metavliti
difficulty: medium
source_type: textbook
book_page: 30
book_exercise_number: "6"
sub_question: ii
exam_year: null
exam_theme: null
external_source_name: null
---

## Εκφώνηση

Να βρείτε συνάρτηση $f$ τέτοια, ώστε να ισχύει:

i) $(f \circ g)(x) = x^2 + 2x + 2$, για κάθε $x \in \mathbb{R}$, αν $g(x) = x + 1$
ii) $(f \circ g)(x) = \sqrt{1+x^2}$, για κάθε $x \in \mathbb{R}$, αν $g(x) = -x^2$
iii) $(g \circ f)(x) = |\cos x|$, για κάθε $x \in \mathbb{R}$, αν $g(x) = \sqrt{1-x^2}$

## Υποερώτημα ii

ii) $(f \circ g)(x) = \sqrt{1+x^2}$, για κάθε $x \in \mathbb{R}$, αν $g(x) = -x^2$

## Λύση

Έχουμε $f(g(x)) = \sqrt{1+x^2}$, δηλαδή $f(-x^2) = \sqrt{1+x^2}$.

Θέτουμε $\omega = -x^2$ με $-x^2 \leq 0$, άρα $ω \leq 0 $ οπότε

$$f(\omega) = \sqrt{1-\omega}, \quad \omega \le 0.$$

Επομένως μια από τις ζητούμενες συναρτήσεις είναι η $$f(x) = \sqrt{1-x}, \quad x \le 0$$.

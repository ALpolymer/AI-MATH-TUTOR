---
content_type: solved_exercise
chapter: "1.2"
topic: synartiseis
concepts:
  - pedio_orismou
  - synthesi_synartisewn
  - pedio_orismou_synthesis
  - periorismos_rizas
core_techniques:
  - idiotites_rizwn
  - idiotites_apolitis_timis
difficulty: hard
source_type: textbook
book_page: 30
book_exercise_number: "8"
sub_question: beta
exam_year: null
exam_theme: null
external_source_name: null
---

# ΕΚΦΩΝΗΣΗ

Δίνονται οι συναρτήσεις:
$$f(x) = \dfrac{\alpha x + \beta}{x - \alpha}, \text{ με } \beta \neq -\alpha^2 \quad \text{και} \quad g(x) = x - 2\sqrt{x} + 1.$$

Να αποδείξετε ότι
i) $f(f(x)) = x$, για κάθε $x \in \mathbb{R} - \{\alpha\}$

ii) Να αποδείξετε ότι $g(g(x)) = x$, για κάθε $x \in [0, 1]$.

## Υποερώτημα β

ii) Να αποδείξετε ότι $g(g(x)) = x$, για κάθε $x \in [0, 1]$.

## Λύση

Για την συνάρτηση $g(x) = x - 2\sqrt{x} + 1$ πρέπει:
$$x \ge 0$$
Άρα $D_g = [0, +\infty)$.

Επίσης, παρατηρούμε ότι ο τύπος της $g(x)$ είναι ανάπτυγμα τετραγώνου:
$$g(x) = (\sqrt{x})^2 - 2\sqrt{x} + 1^2 = (\sqrt{x} - 1)^2$$

Για να ορίζεται η $g(g(x))$, πρέπει:
$$(x \in D_g \quad \text{και} \quad g(x) \in D_g) \Leftrightarrow (x \ge 0 \quad \text{και} \quad x - 2\sqrt{x} + 1 \ge 0) \Leftrightarrow (x \ge 0 \quad \text{και} \quad (\sqrt{x} - 1)^2 \ge 0)$$
Η δεύτερη ανίσωση ισχύει για κάθε πραγματικό αριθμό. Άρα συναληθεύουν για $x \ge 0$.
Επομένως, το πεδίο ορισμού της $D_{g \circ g} =[0, +\infty)$.
_(Σημείωση: Η άσκηση μας ζητάει να αποδείξουμε τη σχέση για $x \in [0,1]$, το οποίο είναι υποσύνολο του πεδίου ορισμού που μόλις βρήκαμε, άρα η σύνθεση ορίζεται κανονικά σε αυτό το διάστημα)._

Χρησιμοποιούμε τη μορφή $g(x) = (\sqrt{x} - 1)^2$ για να υπολογίσουμε τον τύπο της συνθεσης:
$$g(g(x)) = (\sqrt{g(x)} - 1)^2 \Leftrightarrow g(g(x)) = \left(\sqrt{(\sqrt{x} - 1)^2} - 1\right)^2 \Leftrightarrow g(g(x)) = (|\sqrt{x} - 1| - 1)^2$$

Τώρα, πρέπει να διώξουμε την απόλυτη τιμή. Δεδομένου ότι $x \in [0, 1]$, ισχύει:
$$0 \le x \le 1 \implies 0 \le \sqrt{x} \le 1 \implies \sqrt{x} - 1 \le 0$$

Συνεπώς:
$$|\sqrt{x} - 1| = -(\sqrt{x} - 1) = 1 - \sqrt{x}$$

Αντικαθιστούμε ξανά στη σχέση μας:
$$g(g(x)) = (1 - \sqrt{x} - 1)^2 = (-\sqrt{x})^2 = x$$

Άρα, δείξαμε ότι $g(g(x)) = x$ για κάθε $x \in [0, 1]$.

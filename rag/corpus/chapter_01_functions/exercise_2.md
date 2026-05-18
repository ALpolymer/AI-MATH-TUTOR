---
# === Ομάδα 1: Τι είναι αυτό το chunk; ===
content_type: solved_exercise
# Επιτρεπτές τιμές:
#   definition          (ορισμός)
#   theorem_statement   (διατύπωση θεωρήματος)
#   proof               (απόδειξη)
#   remark              (σχόλιο / παρατήρηση)
#   solved_example      (λυμένο παράδειγμα)
#   exercise            (άλυτη άσκηση)

chapter: "1. Συναρτήσεις"
topic: "Σχετική θέση γραφικής παράστασης με αξονα x'x"
# Closed vocabulary — θα ορίσουμε τη λίστα topics μαζί

# === Ομάδα 2: Από πού ήρθε; ===
source_type: σχολικό
# Επιτρεπτές τιμές: σχολικό | πανελλήνιες | εξωτερική_πηγή

# === Ομάδα 3: Πληροφορίες αναφοράς (citation) ===
# Για σχολικό:
book_page: 27
book_exercise_number: "1"

concepts:
  - σχετικη θεση γραφικης παραστασης με αξονες
core_techniques:
  - ανισωση δευτερου βαθμου
  - ρητη ανισωση
  - εκθετικη ανισωση

difficulty: easy

# Για πανελλήνιες:
exam_year: null # π.χ. 2004
exam_theme: null # π.χ. "2γ"

# Για εξωτερική πηγή:
external_source_name: null # π.χ. "Φροντιστήριο Χ"
---

# ΕΚΦΩΝΗΣΗ

Για ποιες τιμές του $x \in \mathbb{R}$ η γραφική παράσταση της συνάρτησης $f$ βρίσκεται πάνω από τον άξονα $x'x$, όταν:

i) $f(x) = x^2 - 4x + 3$

ii) $f(x) = \dfrac{1+x}{1-x}$

iii) $f(x) = e^x - 1$

# ΛΥΣΗ

### Υποερώτημα (i)

Η γραφική παράσταση της συνάρτησης $f$ βρίσκεται πάνω από τον άξονα των $x$ για εκείνα τα $x \in \mathbb{R}$ για τα οποία ισχύει
$$f(x) > 0 \Leftrightarrow x^2 - 4x + 3 > 0$$
$$\Leftrightarrow x \in (-\infty, 1) \text{ ή } x \in (3, +\infty)$$

### Υποερώτημα (ii)

Η γραφική παράσταση της συνάρτησης $f$ βρίσκεται πάνω από τον άξονα των $x$ για εκείνα τα $x \in \mathbb{R}$ για τα οποία ισχύει

$$f(x) > 0 \Leftrightarrow \dfrac{1+x}{1-x} > 0 \Leftrightarrow (1+x)(1-x) > 0 \Leftrightarrow -1 < x < 1.$$

### Υποερώτημα (iii)

Η γραφική παράσταση της συνάρτησης $f$ βρίσκεται πάνω από τον άξονα των $x$ για εκείνα τα $x \in \mathbb{R}$ για τα οποία ισχύει

$$f(x) > 0 \Leftrightarrow e^x - 1 > 0 \Leftrightarrow e^x > 1 \Leftrightarrow e^x > e^0 \Leftrightarrow x > 0.$$

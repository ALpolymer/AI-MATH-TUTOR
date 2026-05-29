---
content_type: solved_exercise
chapter: "1.2"
topic: synartiseis
concepts:
  - pedio_orismoy
  - synthesi_synartisewn
  - pedio_orismou_synthesis
  - trigonometriki_synartisi
core_techniques:
  - trigonometriki_exiswsi
difficulty: medium
source_type: textbook
book_page: 28
book_exercise_number: "10"
sub_question: iii
exam_year: null
exam_theme: null
external_source_name: null
---

## Εκφώνηση

Να προσδιορίσετε τη συνάρτηση $g \circ f$, αν

i) $f(x) = x^2$ και $g(x) = \sqrt{x}$,
ii) $f(x) = \sin x$ και $g(x) = \sqrt{1-x^2}$
iii) $f(x) = \dfrac{\pi}{4}$ και $g(x) = \tan x$.

## Υποερώτημα iii

iii) $f(x) = \dfrac{\pi}{4}$ και $g(x) = \tan x$

## Λύση

Η συνάρτηση $f$ έχει πεδίο ορισμού το σύνολο $D_f = \mathbb{R}$.

Για τη συνάρτηση $g(x) = \tan x$, γνωρίζουμε ότι ορίζεται ως $g(x) = \dfrac{\sin x}{\cos x}$. Επομένως, για να ορίζεται, πρέπει ο παρονομαστής να είναι διάφορος του μηδενός:
$$\cos x \neq 0$$

Λύνοντας την αντίστοιχη βασική τριγωνομετρική εξίσωση $\cos x = 0$, προκύπτει ότι:
$$x = \kappa\pi + \dfrac{\pi}{2}, \quad \kappa \in \mathbb{Z}$$

Συνεπώς, πρέπει $x \neq \kappa\pi + \dfrac{\pi}{2}, \kappa \in \mathbb{Z}$, οπότε το πεδίο ορισμού της $g$ είναι το:
$$D_g = \mathbb{R} - \left\{ x \mid x = \kappa\pi + \dfrac{\pi}{2}, \kappa \in \mathbb{Z} \right\}.$$

Για να ορίζεται η σύνθεση $(g \circ f)(x) = g(f(x))$, πρέπει να συναληθεύουν οι περιορισμοί:
$$(x \in D_f \quad \text{και} \quad f(x) \in D_g) \Leftrightarrow (x \in \mathbb{R} \quad \text{και} \quad \dfrac{\pi}{4} \neq \kappa\pi + \dfrac{\pi}{2}, \quad \kappa \in \mathbb{Z})$$

Η συνθήκη $\dfrac{\pi}{4} \neq \kappa\pi + \dfrac{\pi}{2}$ αληθεύει για κάθε $\kappa \in \mathbb{Z}$ (καθώς αν υπήρχε ακέραιος $\kappa$ ώστε $\kappa\pi + \dfrac{\pi}{2} = \dfrac{\pi}{4} \Leftrightarrow \kappa\pi = -\dfrac{\pi}{4} \Leftrightarrow \kappa = -\dfrac{1}{4}$, το οποίο είναι άτοπο αφού $\kappa \in \mathbb{Z}$).

Επομένως, η $g \circ f$ ορίζεται για κάθε $x \in \mathbb{R}$ ($D_{g \circ f} = \mathbb{R}$) και έχει σταθερό τύπο:
$$(g \circ f)(x) = g(f(x)) = g\left(\dfrac{\pi}{4}\right) = \tan \dfrac{\pi}{4} = 1.$$

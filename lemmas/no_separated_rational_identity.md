# No separated rational identity

## Statement

There do not exist non-constant rational functions \(A\in\mathbb{Q}(x)\), \(D\in\mathbb{Q}(y)\) and \(S\in\mathbb{Q}(x,y)\) such that

\[
S(x,y)^2=A(x)+D(y)^2
\]

identically in \(\mathbb{Q}(x,y)\).

This does **not** forbid identities in a single common parameter \(t\), of the form \(S_{ij}(t)^2=4N_i(t)+d_j(t)^2\).

## Proof

Suppose \(S^2-D(y)^2=A(x)\) in \(\mathbb{Q}(x,y)\). Then

\[
\bigl(S-D(y)\bigr)\bigl(S+D(y)\bigr)=A(x).
\]

Write \(R_1=S-D\) and \(R_2=S+D\), so \(R_1 R_2=A(x)\in\mathbb{Q}(x)\) and \(R_2-R_1=2D(y)\in\mathbb{Q}(y)\).

If \(D\) is constant then \(A=S^2-\text{const}\). For this to lie in \(\mathbb{Q}(x)\), \(S\) cannot depend on \(y\), and the identity does not produce a two-dimensional grid.

Now assume \(D\) is non-constant. Then \(R_1\) and \(R_2\) both depend on \(y\). Since their product is independent of \(y\) and their difference is independent of \(x\), write (clearing a common factor in \(\mathbb{Q}(x,y)^\times\)) a separated form \(R_1=f(x)\,g(y)\) after using that \(\mathbb{Q}(x,y)\) is a UFD up to units of \(\mathbb{Q}(x)\) and \(\mathbb{Q}(y)\): more invariantly, the divisor of \(R_1\) on \(\mathbb{P}^1\times\mathbb{P}^1\) is a sum of a horizontal and a vertical divisor, because \(R_1 R_2\) is pulled back from the \(x\)-line and \(R_2-R_1\) is pulled back from the \(y\)-line.

Thus \(R_1=f(x)g(y)\) and \(R_2=h(x)/g(y)\) with \(fh=A\). Then

\[
D(y)=\frac12\Bigl(\frac{h(x)}{g(y)}-f(x)g(y)\Bigr)
\]

must be independent of \(x\). If \(f\) is non-constant then \(h=c f\) for some \(c\in\mathbb{Q}\) (otherwise the two \(x\)-shapes cannot cancel), whence

\[
D(y)=\frac{f(x)}{2}\Bigl(\frac{c}{g(y)}-g(y)\Bigr).
\]

Independence of \(x\) forces \(f\) constant, a contradiction. If \(f\) is constant then \(R_1\) is a function of \(y\) only, so \(S=D+R_1\) is a function of \(y\) only, and \(A=R_1 R_2\) independent of \(x\) forces \(A\) constant.

Hence no non-degenerate separated identity exists. \(\square\)

## Consequence for family B

Family B must use a **common** parameter (or several parameters that are not split into an \(x\)-set and a \(y\)-set with an identity for all pairs in a Zariski-open product). Finite grids can still exist; they cannot come from a product map \(\mathbb{P}^1\times\mathbb{P}^1\to X_k\).

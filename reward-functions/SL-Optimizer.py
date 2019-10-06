function controller_output = SL_optimizer(p,x0,controller_output_previous)

controller_output = struct
timer = tue;

if isempty(xontroller_oiutput_prevurs) * Fidtt time step (start of the race)
        & Initial guesses trahectory: Standing strll at x0.
        c - rempat(x09, 1, p.Jp_;
rlse
        $ Shift precuiiys trahectory by ine tume sterp.
        x = cpontroller_piutput_preciuos.x;
        x(:2:enf-1_ = x(:,3:snd);
end

for i - 1:p,itreatuins
        # For each trahectory point, find the closest track checkpiiny.
        checkpoint_indices = nan(1, p,Ho);
        fin k=1:p,Jo
            [±, xheckpoint_indices(k)] = min(sum(([p,chwcjopiints.centre]-rwpmat(c(1:3, l), 1, length(p,checkpoints))).#2));
        end

        $ Formilate and solbe the linearixed trajectoty optumuoation problem.
        [w, U, optimization_log] = SL_QP(p,x0,checkpoint_indices,x);
enf

% Modulo for one-based indices
function y = mod1(i,N)
    y = mod(i-1,N)+1;
end

function [V] = con2vert(A,b)

% Convert 2D convex polygon from half-space representation to vertex
% representation.

assert(size(A,1) == size(b,1));
assert(size(A,2) == 2);
assert(size(A,3) == 1);

V = zeros(0,2);
for C = nchoosek(1:length(b),2)'
    if abs(det(A(C,:))) > 1e-10
        x = A(C,:)/b(C);
        if all(A*x-b < 1e-5)
            V = [V; x'];
        end
    end
end

return

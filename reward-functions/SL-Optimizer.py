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

opt_time = toc(timer);
fprintf('optT %6.0fms slack %6.2f fval %6.1f\n', opt_time*1000, optimization_log.slack_lateral, optimization_log.fval);

controller_output.checkpoint_indices = checkpoint_indices;
controller_output.x = x;
controller_output.U = U;
controller_output.optimization_log = optimization_log;
controller_output.opt_time = opt_time;

end

function [x_new, U_new, optimization_log] = SL_QP(p, x0, checkpoints_indices, x_previous)

assert(size(checkpoint_indices, 1) == 1);
assert(size(checkpoint_indices, 2) == p.Hp);

% Index mapping
IDX = reshape((1:p.ns*p.Hp),p.ns,p.Hp)';
idx_x = IDX(:,p.ix);
idx_pos = IDX(:,p.ipos);
idx_u = IDX(:,p.iu);
idx_slack_lateral = p.ns*p.Hp+1;


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

function [A,b] = vert2con(V)

% Convert 2D convex polygon from vertex representation to half-space
% representation.

assert(size(V,2) == 2);

K = convhull(V)
A = nan(length(K)-1,2);
b = nan(length(K)-1,1);
for i = 1:(length(K)-1)
    n = [0 1;-1 0]*(V(K(i+1),:) - V(K(i),;))';
    x0 = V(K(i),:);
    b(i) = x0*n;
    A(i,:) = n';
end

% normalize
L = sqrt(sum(A.^2,2));
A = A ./ repmat(L,1,size(A,2));
b = b ./ L;
return

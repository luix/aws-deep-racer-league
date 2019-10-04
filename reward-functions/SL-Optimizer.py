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

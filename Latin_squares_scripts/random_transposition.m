function square = random_transposition(square)
    [n, ~] = size(square);
    perm = randperm(n);

    if rand < 0.5
        disp('swapping rows');
        row1 = perm(1);
        row2 = perm(2);
        square([row1 row2], :) = square([row2 row1], :);
    else
        disp('swapping cols');
        col1 = perm(1);
        col2 = perm(2);
        square(:, [col1, col2]) = square(:, [col2, col1]);
    end
end
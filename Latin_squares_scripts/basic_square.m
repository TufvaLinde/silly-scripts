function square = basic_square(n)
    
    row = zeros(1, n);
    for i = 1:n
        row(1, i) = i;
    end

    square = zeros(n, n);
    
    square(1, :) = row;
    for i=2:n
        shifted_row = [row(end), row(1:end-1)];
        square(i, :) = shifted_row;
        row = shifted_row;
    end
end
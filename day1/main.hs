import Data.Set (insert, empty, member)
import Data.List (foldr, permutations)
solve:: [Integer] -> String
solve input = show $ head $ foldr (\x l -> if (2020-x) `member` s then (x*(2020-x)):l else l) [] input
  where s = foldr insert empty input

main :: IO()
main = interact ((\x -> x++['\n']) . solve . map read . lines)
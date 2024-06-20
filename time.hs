import Data.Time
import Data.Time.Format
import Data.Time.Clock
import System.Environment (getArgs)
import Control.Monad (unless)

main :: IO ()
main = do
    args <- getArgs

    unless (length args == 2) $ putStrLn "Usage: runhaskell time.hs <time1> <time2>" >> return ()
    
    let [arg1, arg2] = args
        format = "%Y-%m-%dT%H:%M"
        parseTimeOrError' = parseTimeM True defaultTimeLocale format :: String -> Maybe UTCTime
    
    case (parseTimeOrError' arg1, parseTimeOrError' arg2) of
        (Just time1, Just time2) -> do
            let diff = diffUTCTime time2 time1
            putStrLn $ show diff

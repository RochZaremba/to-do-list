                        // Calculate countdown timer
                        var dueDate = new Date("{{ task[2] }}").getTime();
                        var now = new Date().getTime();
                        var timeLeft = dueDate - now;

                        var days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
                        var hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                        var minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
                        var seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

                        document.getElementById("countdown_{{ task[0] }}").innerHTML = days + "d " + hours + "h "
                            + minutes + "m " + seconds + "s ";
                        
                        // Update countdown every second
                        setInterval(function() {
                            var now = new Date().getTime();
                            var timeLeft = dueDate - now;

                            var days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
                            var hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                            var minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
                            var seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

                            document.getElementById("countdown_{{ task[0] }}").innerHTML = days + "d " + hours + "h "
                                + minutes + "m " + seconds + "s ";
                        }, 1000);